/*
  Ref:
  * https://llvm.org/doxygen/
  * https://llvm.org/docs/GettingStarted.html
  * https://llvm.org/docs/WritingAnLLVMPass.html
  * https://llvm.org/docs/ProgrammersManual.html
 */
#include "lab-pass.h"
#include "llvm/IR/LegacyPassManager.h"
#include "llvm/IR/Module.h"
#include "llvm/IR/BasicBlock.h"
#include "llvm/IR/IRBuilder.h"
#include "llvm/IR/Constants.h"
#include "llvm/Analysis/CallGraph.h"
#include "llvm/IR/Function.h"
#include "llvm/Pass.h"
#include "llvm/Support/raw_ostream.h"
#include "llvm/IR/CFG.h"
#include "llvm/ADT/DepthFirstIterator.h"
#include "llvm/ADT/GraphTraits.h"
#include "llvm/IR/Instructions.h"


using namespace llvm;

char LabPass::ID = 0;

bool LabPass::doInitialization(Module &M) {
  return true;
}

static Constant* getI8StrVal(Module &M, char const *str, Twine const &name) {
  LLVMContext &ctx = M.getContext();

  Constant *strConstant = ConstantDataArray::getString(ctx, str);

  GlobalVariable *gvStr = new GlobalVariable(M, strConstant->getType(), true,
  GlobalValue::InternalLinkage, strConstant, name);

  Constant *zero = Constant::getNullValue(IntegerType::getInt32Ty(ctx));
  Constant *indices[] = { zero, zero };
  Constant *strVal = ConstantExpr::getGetElementPtr(Type::getInt8PtrTy(ctx),
  gvStr, indices, true);

  return strVal;
}

static void dumpIR(Function &F)
{
  for (auto &BB : F) {
    errs() << "BB: " << "\n";
    errs() << BB << "\n";
  }
}

static FunctionCallee printfPrototype(Module &M) {
  LLVMContext &ctx = M.getContext();

  FunctionType *printfType = FunctionType::get(
    Type::getInt32Ty(ctx),
    { Type::getInt8PtrTy(ctx) },
    true);

  FunctionCallee printfCallee = M.getOrInsertFunction("printf", printfType);

  return printfCallee;
}


bool LabPass::runOnModule(Module &M) {
  errs() << "runOnModule\n";

  LLVMContext &ctx = M.getContext();
  
  FunctionCallee printfCallee = printfPrototype(M);
  
  GlobalVariable * gvar = new GlobalVariable(M, IntegerType::get(ctx, 32),false,GlobalValue::ExternalLinkage,nullptr,"depth");  
  ConstantInt* const_int_val = ConstantInt::get(ctx, APInt(32,0));
  gvar->setInitializer(const_int_val);

  for (auto &F : M) {

    errs() << F.getName() << "\n";

    if (!F.empty()) { // 檢查函數是否為空
      BasicBlock &Bstart = F.front(); 
      BasicBlock &Bend = F.back(); 
      
      if (!Bstart.empty()) { 
        Instruction &Istart = Bstart.front();
        IRBuilder<> IR(&Istart);
        LoadInst *Load = IR.CreateLoad(Type::getInt32Ty(ctx),gvar);
        Value *Inc = IR.CreateAdd(IR.getInt32(1), Load);
        StoreInst *Store = IR.CreateStore(Inc, gvar);
      }
      
      if (!Bend.empty()) { // 檢查基本塊是否為空
        // Create epilogue BB before ret BB
        BasicBlock *Bepi = BasicBlock::Create(ctx, "epi", &F, &Bend); 
        // Insert code at epilogue
        IRBuilder<> BuilderEnd(Bepi);

        Value *val = BuilderEnd.CreateLoad(Type::getInt32Ty(ctx), gvar);
        // BuilderEnd.CreateCall(printfCallee, { BuilderEnd.CreateGlobalStringPtr("%d "), val });
        if(F.getName()!="main"){
          Value *Space = ConstantInt::get(Type::getInt8Ty(ctx), ' ');
          std::vector<Value *> Args;
          Args.push_back(BuilderEnd.CreateGlobalStringPtr("%*c"));  // 設定格式字串
          Args.push_back(val);  // 設定寬度
          Args.push_back(BuilderEnd.CreateBitCast(Space, Type::getInt32Ty(ctx)));
          BuilderEnd.CreateCall(printfCallee, Args);
        }
        
        BuilderEnd.CreateCall(printfCallee, { getI8StrVal(M, (F.getName() + ": %p\n").str().c_str(), "Msg"), BuilderEnd.CreatePtrToInt(&F, Type::getInt64Ty(ctx)) });
        Instruction &Istart = Bend.back();
        IRBuilder<> IR(&Istart);
        LoadInst *Load = IR.CreateLoad(Type::getInt32Ty(ctx),gvar);
        Value *Inc = IR.CreateAdd(BuilderEnd.getInt32(-1), Load);
        StoreInst *Store = IR.CreateStore(Inc, gvar);
        BuilderEnd.CreateBr(&Bend);
      }
    }
  }

  return true;
}

static RegisterPass<LabPass> X("labpass", "Lab Pass", false, false);
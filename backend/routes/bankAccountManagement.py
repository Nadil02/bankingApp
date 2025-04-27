from fastapi import APIRouter
from services.bankAccountManagement import getBankAccountDetails, removeBankAccount, addBankAccount, otp_validation_account_add, resend_otp_account_add, get_all_banks
from schemas.bankAccountManagement import AccountRemove, AccountAdd,BankAccount, BankAccountAddResponse, OtpRequestAccountAdding, OtpRequestAccountAddingResend, OtpResponseAccountAdding, OtpResponseAccountAddingResend,RemoveAccountResponse, BankListResponse

router = APIRouter(prefix="/bankAccountManagement", tags=["bankAccountManagement"])

@router.get("/accountDetails", response_model=list[BankAccount])
async def get(user_id: int):
    return await getBankAccountDetails(user_id)

@router.post("/removeBankAccount", response_model=RemoveAccountResponse)
async def removeAccount(user_id: int, request: AccountRemove):  
    return await removeBankAccount(user_id, request)

@router.post("/addBankAccount", response_model=BankAccountAddResponse)
async def addAccount(user_id: int, request: AccountAdd):
    return await addBankAccount(user_id, request)

@router.post("/otpAccountAdding", response_model=OtpResponseAccountAdding)
async def otpAdding(request: OtpRequestAccountAdding):
    return await otp_validation_account_add(request)

@router.post("/resendOtpAccountAdding", response_model=OtpResponseAccountAddingResend)
async def resendOtpAdding(request: OtpRequestAccountAddingResend):
    return await resend_otp_account_add(request)

@router.get("/getAllBanks", response_model=BankListResponse)
async def fetch_all_banks():
    try:
        banks = await get_all_banks()
        if not banks:
            return BankListResponse(
                status="success",
                message="No banks found",
                data=[]
            )
        return BankListResponse(
            status="success",
            message="Banks retrieved successfully",
            data=banks
        )
    except Exception as e:
        return BankListResponse(
            status="error",
            message=str(e),
            data=None
        )
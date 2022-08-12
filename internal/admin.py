from fastapi import APIRouter, Depends, Request, Response, HTTPException, status
from support.dependencies import verify_admin_token
from support.schemas import AdminBase


router = APIRouter(
    prefix='/admin',
    tags=['Admin'],
    dependencies=[Depends(verify_admin_token)]
)


@router.post('/', status_code=status.HTTP_200_OK, summary='Example admin')
async def example_admin(request: Request, response: Response, item: AdminBase):
    '''
    Description

    Inputs:
    - **variable_name [dtype]**: description

    Outputs:
    - **variable_name [dtype]**: description
    '''

    print(f'\033[35;1m Request received from: {request.client.host}\033[0m')

    try:
        if item.id == 'admin':
            return {
                'error': False,
                'data': 'Example succeeded'
            }

        else:
            return {
                'error': False,
                'data': 'Example failed'
            }

    except Exception as error:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=error
        )

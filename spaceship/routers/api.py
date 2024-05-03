from fastapi import APIRouter
import numpy as np

router = APIRouter()

@router.get('')
def hello_world() -> dict:
    ma = np.random.rand(10,10)
    mb = np.random.rand(10,10)
    product = np.multiply(ma, mb)
    return {
        'matrix_a': ma.tolist(),
        'matrix_b': mb.tolist(),
        'product': product.tolist()
    }

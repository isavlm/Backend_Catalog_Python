from fastapi import APIRouter, Depends, HTTPException

from app.src.use_cases import (
    ListProducts,
    ListProductResponse,
    FindProductById,
    FindProductByIdResponse,
    FindProductByIdRequest,
    CreateProduct,
    CreateProductResponse,
    CreateProductRequest,
    DeleteProductResponse,
    DeleteProductRequest,
    DeleteProduct,
    UpdateProduct,
    UpdateProductResponse,
    UpdateProductRequest,
    FilterProductByStatus,
    FilterProductsByStatusResponse,
    FilterProductsByStatusRequest
)
from ..dtos import (
    ProductBase,
    ListProductResponseDto,
    CreateProductRequestDto,
    CreateProductResponseDto,
    FindProductByIdResponseDto,
    UpdateProductResponseDto,
    UpdateProductRequestDto,
    FilterProductByStatusResponseDto,
    FilterProductsByStatusRequestDto

)
from factories.use_cases import (
    list_product_use_case,
    find_product_by_id_use_case,
    create_product_use_case,
    delete_product_use_case,
    Update_product_use_case,
    filter_product_use_case,
)

product_router = APIRouter(prefix="/products")


@product_router.get("/", response_model=ListProductResponseDto)
async def get_products(
    use_case: ListProducts = Depends(list_product_use_case),
) -> ListProductResponse:
    response_list = use_case()
    response = [
        {**product._asdict(), "status": str(product.status.value)}
        for product in response_list.products
    ]
    response_dto: ListProductResponseDto = ListProductResponseDto(
        products=[ProductBase(**product) for product in response]
    )
    return response_dto

#Route to filter by status

@product_router.get("/filter-by{filter_by_status}", response_model=FilterProductByStatusResponseDto)
async def filter_product_by_status(
    status: str, 
    use_case: FilterProductByStatus = Depends(filter_product_use_case)  # Use the use case to filter products by status
) -> FilterProductByStatusResponseDto:
    # Create the request with the status
    response = use_case(FilterProductsByStatusRequest(status=status))
    
    if response.products:
        # Convert the response to FilterProductByStatusResponseDto
        return FilterProductByStatusResponseDto(
            products=[
                ProductBase(
                    product_id=product.product_id,
                    user_id=product.user_id,
                    name=product.name,
                    description=product.description,
                    price=product.price,
                    location=product.location,
                    status=product.status,
                    is_available=product.is_available
                )
                for product in response.products
            ]
        )
    else:
        raise HTTPException(status_code=404, detail="No products found with this status")

@product_router.get("/{product_id}", response_model=FindProductByIdResponseDto)
async def get_product_by_id(
    product_id: str, use_case: FindProductById = Depends(find_product_by_id_use_case)
) -> FindProductByIdResponse:
    response = use_case(FindProductByIdRequest(product_id=product_id))
    response_dto: FindProductByIdResponseDto = FindProductByIdResponseDto(
        **response._asdict()
    )
    return response_dto


@product_router.post("/", response_model=CreateProductResponseDto | str)
async def create_product(
    request: CreateProductRequestDto,
    use_case: CreateProduct = Depends(create_product_use_case),
) -> CreateProductResponse:
    if request.status not in ["New", "Used", "For parts"]:
        return "Not a valid status value (New, Used, For parts)"
    response = use_case(
        CreateProductRequest(
            product_id=request.product_id,
            user_id=request.user_id,
            name=request.name,
            description=request.description,
            price=request.price,
            location=request.location,
            status=request.status,
            is_available=request.is_available,
        )
    )
    response_dto: CreateProductResponseDto = CreateProductResponseDto(
        **response._asdict()
    )
    return response_dto


# Isadora's code starts here.

#ROUTE TO DELETE
@product_router.delete("/{product_id}", response_model=DeleteProductResponse)
async def delete_product(
    product_id: str, use_case: DeleteProduct = Depends(delete_product_use_case)
) -> DeleteProductResponse:
    response = use_case(DeleteProductRequest(product_id=product_id))
    if response:
        return response
    else:
        raise HTTPException(status_code=404, detail="Product not found")


#Route to Update

@product_router.put("/{product_id}", response_model=updateProductResponseDto)
async def update_product(
    product_id: str, 
    request: updateProductRequestDto,
    use_case: updateProduct = Depends(update_product_use_case),    
) -> updateProductResponseDto | str:
    # Validate product status
    if request.status not in ["New", "Used", "For parts"]:
        raise HTTPException(status_code=400, detail="Not a valid status value (New, Used, For parts)")
    
    # Convert the DTO to the request model expected by the use case
    update_request = updateProductRequest(
        product_id=request.product_id,
        user_id=request.user_id,
        name=request.name,
        description=request.description,
        price=request.price,
        location=request.location,
        status=request.status,
        is_available=request.is_available,
    )
    
    # Call the use case
    response = use_case(product_id, update_request)
    
    if response:
        # Convert the response to updateProductResponseDto
        return updateProductResponseDto(
            product_id=response.product_id,
            user_id=response.user_id,
            name=response.name,
            description=response.description,
            price=response.price,
            location=response.location,
            status=response.status,
            is_available=response.is_available
        )
    else:
        raise HTTPException(status_code=404, detail="Product not found")

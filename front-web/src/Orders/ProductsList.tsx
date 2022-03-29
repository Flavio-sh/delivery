import React from 'react';
import ProductCard from "./ProductCard";
import './styles.css';
import {Product} from "../types";

type Props = {
    products: Product[];
}

export default function ProductsList({ products } : Props) {
    return (
        <div className={"orders-list-container"}>
            <div className={"order-list-items"}>
                {
                    products.map(product => (
                        <ProductCard key={product.id} product={product}/>
                    ))
                }

            </div>

        </div>
    )
}
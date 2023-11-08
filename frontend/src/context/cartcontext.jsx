import { createContext, useReducer } from "react";
import {cartReducer,cartInitialState} from '../reducers/cart.js'

export const CartContext = createContext()

function useCartReducer(){
    const [state, dispatch] = useReducer(cartReducer, cartInitialState)

    const addToCart = product => dispatch({
        type: 'ADD_TO_CART',
        payload: product
    })

    const subtractToCart = product => dispatch({
        type: 'SUBTRACT_TO_CART',
        payload: product
    })

    const removeFromCart = product => dispatch({
        type: 'REMOVE_FROM_CART',
        payload: product
    })

    const clearCart = () => dispatch({
        type: 'CLEAR_CART'
    })

    return {state, addToCart,subtractToCart, removeFromCart , clearCart}
}

export function CartProvider({ children }) {
    const {state, addToCart,subtractToCart, removeFromCart , clearCart} = useCartReducer()

    return (
        <CartContext.Provider value={{
            cart: state,
            addToCart,
            subtractToCart,
            removeFromCart,         
            clearCart,
        }}>
            {children}
        </CartContext.Provider>

    )
}
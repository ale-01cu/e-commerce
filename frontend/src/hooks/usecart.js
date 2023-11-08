import { useContext } from 'react';
import { CartContext } from '../context/cartcontext.jsx';
 

export const userCart =()=>{
    const context = useContext(CartContext)

    if (context === undefined){
        throw new Error ('userCart must be used within a CartProvider / userCart debe usarse dentro de un CartProvider ')

    }

    return context
}
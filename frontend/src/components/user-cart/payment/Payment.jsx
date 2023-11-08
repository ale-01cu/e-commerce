import { useEffect, useState } from 'react'
import './payment.css'
import { userCart } from "../../../hooks/usecart.js";
import { toast } from 'sonner'

export function Payment({ tarifaZona }) {
    const [payment, setPayment] = useState(0)
    const { cart } = userCart();
    let totalPayment = 0;

    useEffect(() => {
        for (let i = 0; i < cart.length; i++) {
            totalPayment += cart[i].count * cart[i].price
        }

        totalPayment = totalPayment + tarifaZona
        setPayment(totalPayment)
    }, [tarifaZona,cart])

    return (
        <>
            <div className='container-payment'>
                <div className="section-payment">

                    <div className="container-ticket">
                        <div className='small-information'>
                            <span className='delibery'>Envio</span>
                            <span className='cost-delibery'>$ {tarifaZona}.00</span>

                        </div>
                        <hr id='hr'></hr>

                        <div className='pay-container'>
                            <div className='total-container'>
                                <span className='total-amount'>Pago Total</span>
                                <span className='total-cost'>CUP {payment}.00</span>
                            </div>
                            
                            <button  onClick={() => toast.success('Event has been created')}>Ordenar</button>

                        </div>
                    </div>
                </div>
            </div>
        </>
    )
}
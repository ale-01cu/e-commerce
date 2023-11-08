import './cart.css'
import { Order } from './order/Order'
import ClearCartIcon from '../../../assets/svg/remove_shopping_cart_FILL0_wght400_GRAD0_opsz24.svg'
import {userCart} from '../../../hooks/usecart'

export function Cart() {
const {clearCart} = userCart()

    return (
        <>
            <div className="section-cart">

                <div className='section-cart__delivery'>
                    <div className="take">
                        <svg xmlns="http://www.w3.org/2000/svg" width="35" height="30" viewBox="0 0 25 26" fill="#1F2937">
                            <path d="M23.5692 8.47405C23.3973 8.30736 23.1927 8.17516 22.9674 8.08512C22.742 7.99508 22.5004 7.94898 22.2564 7.9495H18.547V7.05664C18.547 5.39904 17.8631 3.80933 16.6457 2.63722C15.4283 1.46512 13.7772 0.806641 12.0556 0.806641C10.3339 0.806641 8.68279 1.46512 7.4654 2.63722C6.24802 3.80933 5.5641 5.39904 5.5641 7.05664V7.9495H1.8547C1.3628 7.9495 0.891053 8.13764 0.543229 8.47252C0.195405 8.80741 0 9.26161 0 9.73521V21.7888C0 23.9651 1.91266 25.8066 4.17308 25.8066H19.938C21.0314 25.807 22.0815 25.3954 22.8638 24.6599C23.2575 24.2983 23.571 23.8636 23.7853 23.3822C23.9997 22.9007 24.1105 22.3824 24.1111 21.8585V9.73521C24.1119 9.50094 24.0644 9.26885 23.9713 9.05237C23.8783 8.8359 23.7416 8.63933 23.5692 8.47405ZM7.4188 7.05664C7.4188 5.87264 7.90731 4.73713 8.77687 3.89991C9.64643 3.0627 10.8258 2.59235 12.0556 2.59235C13.2853 2.59235 14.4647 3.0627 15.3342 3.89991C16.2038 4.73713 16.6923 5.87264 16.6923 7.05664V7.9495H7.4188V7.05664ZM18.547 12.4138C18.547 14.0714 17.8631 15.6611 16.6457 16.8332C15.4283 18.0053 13.7772 18.6638 12.0556 18.6638C10.3339 18.6638 8.68279 18.0053 7.4654 16.8332C6.24802 15.6611 5.5641 14.0714 5.5641 12.4138V11.5209C5.5641 11.2841 5.6618 11.057 5.83572 10.8896C6.00963 10.7221 6.2455 10.6281 6.49145 10.6281C6.7374 10.6281 6.97327 10.7221 7.14719 10.8896C7.3211 11.057 7.4188 11.2841 7.4188 11.5209V12.4138C7.4188 13.5978 7.90731 14.7333 8.77687 15.5705C9.64643 16.4077 10.8258 16.8781 12.0556 16.8781C13.2853 16.8781 14.4647 16.4077 15.3342 15.5705C16.2038 14.7333 16.6923 13.5978 16.6923 12.4138V11.5209C16.6923 11.2841 16.79 11.057 16.9639 10.8896C17.1378 10.7221 17.3737 10.6281 17.6196 10.6281C17.8656 10.6281 18.1015 10.7221 18.2754 10.8896C18.4493 11.057 18.547 11.2841 18.547 11.5209V12.4138Z" fill="#1F2937" />
                        </svg>
                        <span> Su orden</span>
                    </div>
                    <button className='clear_cart_icon' title='Limpiar Carrito' onClick={()=>clearCart()}>
                        <img src={ClearCartIcon} alt="" srcset="" className='transitionimg'/>
                    </button>
                </div>

                <Order />
            </div>

        </>
    )
}
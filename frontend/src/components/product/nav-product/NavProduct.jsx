import './navproduct.css'
import { HiddenSectionProduct } from '../../../assets/js/hidden_section_usercar_tablet'
import { Link } from "react-router-dom";
import { useSelector } from "react-redux";
import ImagLogo from '../../../assets/svg/LogoWebMGC.svg'

export function NavProduct() {
    const { isLoggedIn } = useSelector((state) => state.auth);
    return (
        <>
            <nav className='container-product'>

                <img src={ImagLogo} alt="logo"className='imglogo'/>

                {isLoggedIn ?
                    <div onClick={HiddenSectionProduct} className='container-product-option-svg '>
                        <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" strokeWidth={1.5} stroke="currentColor" className="w-6 h-6">
                            <path strokeLinecap="round" strokeLinejoin="round" d="M3.75 6.75h16.5M3.75 12h16.5m-16.5 5.25h16.5" />
                        </svg>
                    </div>
                    :

                    <div className='section_login_register'>
                        <Link to={"/login"} className="section-usercard_login">
                            Iniciar sesión
                        </Link>
                        <Link to={"/register"} className="section-usercard_register">
                            Crear cuenta
                        </Link>
                    </div>
                }

            </nav>
        </>
    )
}
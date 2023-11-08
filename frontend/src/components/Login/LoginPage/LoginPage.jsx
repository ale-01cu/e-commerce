import { Login } from "../LoginFormComponents/LoginForm"
import pan1 from "../../../assets/svg/breadloaf.svg"
import pan2 from "../../../assets/svg/roundbread.svg"
import icecream from "../../../assets/svg/StockImage_ FoodandDrink.svg"
import buycoffe from '../../../assets/svg/buycoffe.svg'
import "./login.css"


export function PageLogin() {
    return (
        <>
            
            <div className="container-login">
             
                <div className="pan1">
                    <img src={pan1} alt="Imagen de Pan1 como fondo de login" />
                </div>

                <div className="pan2">
                    <img src={pan2} alt="Imagen de Pan2 como fondo de login" />
                </div>

                <div className="helado">
                    <img src={icecream} alt="Imagen de Helado como fondo de login" />
                </div>

                <Login />

                <a href="https://api.whatsapp.com/send?phone=5356083106&amp;text=¡Hola, Somos <Dream.Space/>! ¿Necesitas ayuda profesional en programación y diseño? ✨👨‍💻 Somos un equipo joven y entusiasta apasionado por el desarrollo de software. Permítenos ayudarte a materializar tus ideas y crear soluciones innovadoras. ¡Contáctanos ahora! 🚀"
                    className="create-by-dreamspace"
                    target="_blank">

                    <div className="create-by-dreamspace-info" >
                        <p className="buy-coffe-p"> Buy coffe</p>
                        <p className="create-by-p"> Create by {'<Dream.Space/>'} </p>
                    </div>

                    <div className="div-buy-coffe">
                        <img className="buy-coffe-svg" src={buycoffe} alt="Imagen de Helado como fondo de login" />
                    </div>

                </a>

            </div>

        </>
    )
}
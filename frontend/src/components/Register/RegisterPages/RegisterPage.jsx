import { Register } from "../RegisterFormComponents/RegisterForm"
import pan1 from "../../../assets/svg/breadloaf.svg"
import pan2 from "../../../assets/svg/roundbread.svg"
import icecream from "../../../assets/svg/StockImage_ FoodandDrink.svg"
import "./register.css"

export function PageRegister(){
    return(
        
        <div className="container-form">

            <div className="pan1">
                <img src={pan1} alt="" /> 
            </div>
            <div className="pan2">
                <img src={pan2} alt="" />
            </div>
            <div className="helado">
                <img src={icecream} alt="" />
            </div>
            <Register/>

        </div>
        
    )
}
import { Register2 } from "../RegisterForm2Components/RegisterForm2"
import pan1 from "../../../assets/img/breadloaf.svg"
import pan2 from "../../../assets/img/roundbread.svg"
import icecream from "../../../assets/img/StockImage_FoodandDrink.svg"
import "./register2.css"

export function PageRegister2(){
    return(
        
        <div className="container">
            <div className="pan1">
                <img src={pan1} alt="" /> 
            </div>
            <div className="pan2">
                <img src={pan2} alt="" />
            </div>
            <div className="helado">
                <img src={icecream} alt="" />
            </div>
            <Register2/>
        </div>
        
    )
}
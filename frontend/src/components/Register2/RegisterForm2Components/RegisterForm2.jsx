import './registerform2.css'

export function Register2(){

    function OnChange(){
        let button = document.getElementById('next')
        button.classList.add('next')
        let span = document.getElementById('loadingRegister')
        span.classList.add('box-active')
    }


    return(
        <div className="register-form-2-container">
                <h1>Register</h1>
                <form action="">
                    <div className='box-input'>
                        <input type="date" name="register2_date" id="register2_date" required/>
                        <span>Fecha de Nacimiento</span>
                    </div>
                    <div className='box-input'>
                            <input type="password"  name="register2_password" id="register2_password" placeholder="Password" required/>
                            <span>Password</span>
                    </div>
                    <div className='box-input'>
                            <input type="password" name="register2_confirmpassword" id="register2_confirmpassword" placeholder="Confirm password" required/>
                            <span>Confirm password</span>
                    </div>
                    <div className='button-container'>
                        <div id='next' className=''>
                        <button  type="submit" onClick={OnChange} >Save</button>
                        </div>
                        <span id='loadingRegister' className='box'><p></p></span>
                    </div>
                    
                </form>
        </div>
    )
}
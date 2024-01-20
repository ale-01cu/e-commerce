import "./usercard.css";
import { HiddenUserCard } from "../../../assets/js/hiddensection";
import { useSelector, useDispatch } from "react-redux";
import { logout } from "../../../redux/slices/authSlice";
import logoutimg from  '../../../assets/svg/logout_FILL0_wght400_GRAD0_opsz24.svg'

import { BackIcon} from '../../../assets/svg/Icons'

export function UserCard() {
  const { profile } = useSelector((state) => state.profile);
  const dispatch = useDispatch();

  function handleLogout() {
    dispatch(logout());
  }

  return (
    
    <div className='section-usercard'>

      <button 
        title='Ir Atras' 
        className="usercard_backIcon" 
        onClick={HiddenUserCard}
      >
        <BackIcon />
      </button>

      <div className="section-usercard__img">
        {profile.photo ? (
          <img
            className="section-usercard__imgobject"
            src={"http://localhost:8000/" + profile.photo}
            alt="Foto del usuario"
          />

        ) : (

          <span className="section-usercard__chartName" >
            {profile.user.first_name.charAt(0)}
          </span>
        )}
      </div>

      <div className="section_userdate">
        <span>
          {profile.user.first_name} {profile.user.last_name}
        </span>
        <p>{profile.municipality}</p>
      </div>

      <button className="Sign_off" title='Cerrar sesión' onClick={handleLogout}>
        <img src={logoutimg} alt="" srcSet="" />
      </button>

    </div>

  );
}



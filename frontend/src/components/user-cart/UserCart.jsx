import { useState } from 'react'
import './usercart.css'
import { UserCard } from './usercard/UserCard'
import { Cart } from './cart/Cart'
import { Payment } from './payment/Payment'
import { LocationDelivery } from './locationdelivery/LocationDelivery'
import { useSelector } from "react-redux";

export function UserCart() {

  const { isLoggedIn } = useSelector((state) => state.auth);

  const [tarifaZona, setTarifaZona] = useState(0);

  const actualizarTarifa = (nuevaTarifa) => {
    setTarifaZona(nuevaTarifa);
  };

  return (

    <>{isLoggedIn &&

      <div id='container-usercart' className='container-usercart hidden'>
        <aside className='container-usercart-info'>
          <UserCard />
          <Cart />
          <LocationDelivery actualizarTarifa={actualizarTarifa} />
          <Payment tarifaZona={tarifaZona} />
        </aside>
      </div>
      
    }
    </>

  )
}
import { ButtonDelivery } from '../buttons/ButtonDelivery'
import { MultiButtonDelivery } from '../buttons/MultiButtonDelivery'
import './locationdelivery.css'

export function LocationDelivery({actualizarTarifa}) {

    return (
        <>
            <div className='container-locationdelivery'>
                <div className="section-locationdelivery">

                    <div><h4>Entre calles: </h4></div>

                    <div className='section-locationdelivery__street'>
                        <input id='stree-one' type="text" placeholder='Primera calle' required />
                        <p>y</p>
                        <input id='stree-two' type="text" placeholder='Segunda calle' required />
                    </div>

                    <div className='section-locationdelivery-build'>
                        <ButtonDelivery />
                        <input id='house_number' type="text" placeholder='No. Casa' required />
                    </div>

                    <div className='section-locationdelivery-municipality'>
                        <MultiButtonDelivery actualizarTarifa={actualizarTarifa} />
                    </div>

                </div>
            </div>

        </>
    )
}
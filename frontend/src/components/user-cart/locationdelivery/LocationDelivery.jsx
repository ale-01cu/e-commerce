import { ButtonDelivery } from "../buttons/ButtonDelivery";
import { MultiButtonDelivery } from "../buttons/MultiButtonDelivery";
import "./locationdelivery.css";
import { useSelector, useDispatch } from "react-redux";
import {
  set_streetOne,
  set_streetTwo,
  set_houseNumber,
} from "../../../redux/slices/productSlice";

export function LocationDelivery({ actualizarTarifa }) {
  const dispatch = useDispatch();
  const handleStreetone = (e) => {
    dispatch(set_streetOne(e.target.value));
  };
  const handleStreettwo = (e) => {
    dispatch(set_streetTwo(e.target.value));
  };
  const handleHosenumber = (e) => {
    dispatch(set_houseNumber(e.target.value));
  };
  return (
    <>
      <div className="container-locationdelivery">
        <div className="section-locationdelivery">
          <div>
            <h4>Entre calles: </h4>
          </div>

          <div className="section-locationdelivery__street">
            <input
              id="stree-one"
              type="text"
              placeholder="Primera calle"
              onChange={handleStreetone}
              required
            />
            <p>y</p>
            <input
              id="stree-two"
              type="text"
              placeholder="Segunda calle"
              onChange={handleStreettwo}
              required
            />
          </div>

          <div className="section-locationdelivery-build">
            <ButtonDelivery />
            <input
              id="house_number"
              type="text"
              placeholder="No. Casa"
              onChange={handleHosenumber}
              required
            />
          </div>

          <div className="section-locationdelivery-municipality">
            <MultiButtonDelivery actualizarTarifa={actualizarTarifa} />
          </div>
        </div>
      </div>
    </>
  );
}

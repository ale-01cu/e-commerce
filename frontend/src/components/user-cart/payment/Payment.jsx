import { useEffect, useState } from "react";
import { useDispatch, useSelector } from "react-redux";
import "./payment.css";
import { userCart } from "../../../hooks/usecart.js";
import { toast } from "sonner";
import { sendOrder } from "../../../redux/slices/productSlice.js";
export function Payment({ tarifaZona }) {
  const dispatch = useDispatch();
  const [payment, setPayment] = useState(0);
  const { cart } = userCart();
  let totalPayment = 0;
  const { streetOne, streetTwo, houseNumber } = useSelector(
    (state) => state.product
  );
  const { profile } = useSelector((state) => state.profile);
  const { user } = useSelector((state) => state.auth);
  function handlePayment() {
    const order_items = cart.map((x) => {
      return { product: x.id, count: x.count };
    });
    console.log(order_items);
    const first_name = user.first_name;
    const last_name = user.last_name;
    const address_line_1 = "Entre "+streetOne + " y " + streetTwo + " Casa:" + houseNumber;
    const shipping_price = tarifaZona;
    const province = profile.province;
    dispatch(
      sendOrder({
        order_items,
        first_name,
        last_name,
        address_line_1,
        province,
        shipping_price,
      })
    );
  }

  useEffect(() => {
    for (let i = 0; i < cart.length; i++) {
      totalPayment += cart[i].count * cart[i].price;
    }

    totalPayment = totalPayment + tarifaZona;
    setPayment(totalPayment);
  }, [tarifaZona, cart]);

  return (
    <>
      <div className="container-payment">
        <div className="section-payment">
          <div className="container-ticket">
            <div className="small-information">
              <span className="delibery">Envio</span>
              <span className="cost-delibery">$ {tarifaZona}.00</span>
            </div>
            <hr id="hr"></hr>

            <div className="pay-container">
              <div className="total-container">
                <span className="total-amount">Pago Total</span>
                <span className="total-cost">CUP {payment}.00</span>
              </div>

              <button onClick={handlePayment}>Ordenar</button>
            </div>
          </div>
        </div>
      </div>
    </>
  );
}

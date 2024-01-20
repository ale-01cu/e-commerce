import { SectionProduct } from "./components/product/SectionProduct";
import { UserCart } from "./components/user-cart/UserCart";
import { useEffect } from "react";
import { useDispatch } from "react-redux";
import { check_authenticated, refresh } from "./redux/slices/authSlice";
import bread1 from "./assets/svg/breadloaf.svg";
import bread2 from "./assets/svg/roundbread.svg";
import icecream from "./assets/svg/StockImage_ FoodandDrink.svg";
import { CartProvider } from "./context/cartcontext";
import { Toaster } from 'sonner'

function App() {
  const dispatch = useDispatch();
  useEffect(() => {
    dispatch(refresh())
    dispatch(check_authenticated());
  }, [dispatch]);
  return (
    <>
      <div className="container ">
      <Toaster position="top-center" expand={true}  />
        <img className="bread1" src={bread1} alt="" />
        <img className="bread2" src={bread2} alt="" />
        <img className="icecream" src={icecream} alt="" />
        <CartProvider>
          <main className="main-container">
            <SectionProduct />
            <UserCart />
          </main>
        </CartProvider>
      </div>
    </>
  );
}

export default App;

import "./card.css";
import helado from "../../../assets/svg/StockImage_ FoodandDrink.svg";
import {
  AddToCartIcon,
  RemoveFromCartIcon,
} from "../../../assets/svg/Icons.jsx";
import { useSelector } from "react-redux";

export function Card({
  photo,
  description,
  name,
  price,
  isProductInCart,
  countProductoInCart,
  addToCart,
  subtractToCart,
  removeFromCart,
}) {
  const { isLoggedIn } = useSelector((state) => state.auth);
  return (
    <div className="card">
      <img src={photo} alt="" className="img" />
      <div className="information">
        <h4>{name}</h4>
        <div className="ingredients">
          <p>{description}</p>
        </div>
      </div>
      <div className="cant">
        {isLoggedIn && (
          <>
            <div title="Sumar producto del carrito" className="plus">
              <button onClick={addToCart}>+</button>
            </div>
            <span className="value">{countProductoInCart}</span>
            <div title="Sustraer producto del carrito" className="down">
              <button onClick={subtractToCart}>-</button>
            </div>
          </>
        )}
      </div>
      <div className="section-likes">
        <span> $ {price} </span>

        {isLoggedIn && (
          <button
            className="btnpago"
            title={
              isProductInCart
                ? "Eliminar Producto del carrtio"
                : "Añadir producto del carrito"
            }
            style={{
              backgroundColor: isProductInCart ? "#f9d5c1" : "#000",
              color: isProductInCart ? "#000" : "#fff",
            }}
            onClick={isProductInCart ? removeFromCart : addToCart}
          >
            {isProductInCart ? <RemoveFromCartIcon /> : <AddToCartIcon />}
          </button>
        )}
      </div>
    </div>
  );
}

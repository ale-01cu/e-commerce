import { userCart } from "../../../../hooks/usecart.js";
import "./order.css";

export function Order() {
  const { cart } = userCart();

  return (
    <div className="section-order">
      {cart.map((product) => (
        <CartItem
          key={product.id}
          // countProductoInCart={countProductoInCart(product)}
          {...product}
        />
      ))}
    </div>
  );
}

function CartItem({
  name,
  count,
  category,
  price,
  photo, 
}) {
  return (
    <>
      <div className="container-order">
        <img
          className="image_product"
          src={photo} // photo del producto
          alt={name} // description del tipo de producto( Category + name(sabor))
        />

        <div className="section_datos">
          <h3>{name}</h3> {/*sabor del helado */}
          {category === "Helados" ? (
            <p> {count} Tinas de helado</p>
          ) : (
            <p> {count} Bolsa de panes</p>
          )}
          {/* Buscar como estructurar este texto   {countProductoInCart} */}
        </div>
        <div className="price">
          <span>$ {price * count}</span>
        </div>
      </div>
    </>
  );
}

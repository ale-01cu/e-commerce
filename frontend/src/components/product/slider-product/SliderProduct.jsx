import "./sliderproduct.css";
import { Card } from "../card/card";
import Carousel from "react-multi-carousel/lib/Carousel";
import "react-multi-carousel/lib/styles.css";
import { userCart } from "../../../hooks/usecart.js";
import { useSelector } from "react-redux";

export function SliderProduct() {

  const { cart, addToCart, subtractToCart, removeFromCart } = userCart();

  const checkProductInCart = (product) => {
    return cart.some((item) => item.id === product.id);
  };

  const countProductoInCart = (product) => {
    const index = cart.findIndex((item) => item.id === product.id);
    if (index >= 0) {
      return cart[index].count;
    }
    return 0;
  };
  const { products } = useSelector((state) => state.product);

  return (
    <>
      <div className="slider_container">
        <Carousel
          additionalTransfrom={0}
          arrows
          autoPlaySpeed={4000}
          centerMode={false}
          className=""
          containerClass="container-with-dots"
          dotListClass=""
          // draggable
          focusOnSelect={false}
          infinite
          itemClass=""
          keyBoardControl
          responsive={{
            desktop: {
              breakpoint: {
                max: 9999999,
                min: 1440,
              },
              items: 5,
              partialVisibilityGutter: 40,
            },
            minipc: {
              breakpoint: {
                max: 1439,
                min: 960,
              },
              items: 4,
              partialVisibilityGutter: 30,
            },
            tablet: {
              breakpoint: {
                max: 960,
                min: 750,
              },
              items: 3,
              partialVisibilityGutter: 30,
            },
            minitablet: {
              breakpoint: {
                max: 750,
                min: 480,
              },
              items: 2,
              partialVisibilityGutter: 30,
            },
            mobile: {
              breakpoint: {
                max: 480,
                min: 0,
              },
              items: 1,
              partialVisibilityGutter: 30,
            },
          }}
          showDots={false}
          sliderClass=""
          slidesToSlide={1}
          swipeable
        >
          {products.map((product) => (
            <Card
              key={product.id}
              addToCart={() => addToCart(product)}
              subtractToCart={() => subtractToCart(product)}
              removeFromCart={() => removeFromCart(product)}
              countProductoInCart={countProductoInCart(product)}
              isProductInCart={checkProductInCart(product)}
              {...product}
            />
          ))}
        </Carousel>
      </div>
    </>
  );
}

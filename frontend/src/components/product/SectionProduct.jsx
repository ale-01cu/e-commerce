import { Category } from "./category/Category";
import { NavProduct } from "./nav-product/NavProduct";
import { SliderProduct } from "./slider-product/SliderProduct";
import { useEffect } from "react";
import "./sectionproduct.css";
import { useDispatch, useSelector } from "react-redux";
import {
  getProduct_icecream,
  getProduct_bread,
  getProduct,
  set_focusedProduct,
} from "../../redux/slices/productSlice";

export function SectionProduct() {
  const { isLoggedIn } = useSelector((state) => state.auth);

  const { focusedProduct } = useSelector((state) => state.product);
  const dispatch = useDispatch();

  function handlefocusicecream() {
    if (focusedProduct != "icecream") {
      dispatch(set_focusedProduct("icecream"));
      dispatch(getProduct_icecream());
    }
  }

  function handlefocusbread() {
    if (focusedProduct != "bread") {
      dispatch(set_focusedProduct("bread"));
      dispatch(getProduct_bread());
    }
  }

  useEffect(() => {
    if (focusedProduct === "icecream") {
      dispatch(getProduct_icecream());
    } else if (focusedProduct === "bread") {
      dispatch(getProduct_bread());
    } else {
      dispatch(getProduct());
    }
  }, [dispatch]);

  return (
    <section id="section-product" className={isLoggedIn ? 'section-product' : 'section-product_isLoggedIn'}>
      <NavProduct />
      <Category
        handleClickI={handlefocusicecream}
        handleClickB={handlefocusbread}
      />
      <SliderProduct />
    </section>
  );
}

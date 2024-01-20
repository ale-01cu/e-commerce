import axios from "axios";

const API_URL = "http://localhost:8000/";
const check_product_all = () => {
  return axios
    .get(API_URL + "/api/products/", {
      headers: {
        "Content-Type": "application/json",
      },
    })
    .then((response) => {
      return response.data;
    });
};
const check_category_all = () => {
  return axios
    .get(API_URL + "/api/categorys/", {
      headers: {
        "Content-Type": "application/json",
      },
    })
    .then((response) => {
      return response.data;
    });
};
const check_product_icecream = () => {
  return axios
    .get(API_URL + "/api/products/?category=1", {
      headers: {
        "Content-Type": "application/json",
      },
    })
    .then((response) => {
      return response.data;
    });
};
const check_product_bread = () => {
  return axios
    .get(API_URL + "/api/products/?category=2", {
      headers: {
        "Content-Type": "application/json",
      },
    })
    .then((response) => {
      return response.data;
    });
};
const save_order = (
  order_items,
  first_name,
  last_name,
  address_line_1,
  province,
  shipping_price
) => {
  const access = JSON.parse(localStorage.getItem("access"));
  return axios
    .post(
      API_URL + "/api/orders/",
      {
        order_items,
        first_name,
        last_name,
        address_line_1,
        province,
        shipping_price,
      },
      {
        headers: {
          Authorization: "Bearer " + access,
          Accept: "application/json",
        },
      }
    )
    .then((response) => {
      return response.data;
    });
};

const ProductService = {
  check_product_all,
  check_product_icecream,
  check_product_bread,
  save_order,
  check_category_all
};

export default ProductService;

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
const check_product_icecream = () => {
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
const check_product_bread = () => {
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
const save_order=()=>{
  
}

const ProductService = { check_product_all,check_product_icecream,check_product_bread };

export default ProductService;

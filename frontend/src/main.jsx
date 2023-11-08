import React from "react";
import ReactDOM from "react-dom/client";
import App from "./App.jsx";
import "./main.css";
import { BrowserRouter, Route, Routes } from "react-router-dom";
import { store } from "./redux/store/store.js";
import { Provider } from "react-redux";
import { PageLogin } from "./components/Login/LoginPage/LoginPage.jsx";
import { PageRegister } from "./components/Register/RegisterPages/RegisterPage.jsx";
import  Activate  from "./components/Activate/Activate.jsx";
ReactDOM.createRoot(document.getElementById("root")).render(
  <Provider store={store}>
    <BrowserRouter>
      <Routes>
        <Route path="/" element={<App />}></Route>
        <Route path="/login" element={<PageLogin />}></Route>
        <Route path="/register" element={<PageRegister />}></Route>
        <Route path="/activate/:uid/:token" element={<Activate />}></Route>
      </Routes>
    </BrowserRouter>
  </Provider>
);

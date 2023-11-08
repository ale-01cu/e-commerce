import { configureStore } from "@reduxjs/toolkit";
import messageReducer from "../slices/messageSlice";
import authReducer from "../slices/authSlice";
import profileReducer from "../slices/profileSlice";
import productReducer from "../slices/productSlice";
export const store = configureStore({
  reducer: {
    auth: authReducer,
    message: messageReducer,
    profile: profileReducer,
    product: productReducer,
  },
});

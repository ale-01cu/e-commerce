import { createAsyncThunk, createSlice } from "@reduxjs/toolkit";
import ProductService from "../../services/product.service";

export const getProduct = createAsyncThunk(
  "product/getProduct",
  async (_, thunkAPI) => {
    try {
      const data = await ProductService.check_product_all();
      return data;
    } catch {
      return thunkAPI.rejectWithValue();
    }
  }
);
export const getProduct_icecream = createAsyncThunk(
  "product/getProduct_icecream",
  async (_, thunkAPI) => {
    try {
      const data = await ProductService.check_product_icecream();
      return data;
    } catch {
      return thunkAPI.rejectWithValue();
    }
  }
);
export const getProduct_bread = createAsyncThunk(
  "product/getProduct_bread",
  async (_, thunkAPI) => {
    try {
      const data = await ProductService.check_product_bread();
      return data;
    } catch {
      return thunkAPI.rejectWithValue();
    }
  }
);

const productSlice = createSlice({
  name: "product",
  initialState: { products: [], focusedProduct: "icecream" },
  reducers: {
    set_focusedProduct: (state, action) => {
      state.focusedProduct = action.payload;
    },
  },
  extraReducers: (builder) => {
    builder
      .addCase(getProduct.fulfilled, (state, action) => {
        state.products = action.payload;
      })
      .addCase(getProduct_icecream.fulfilled, (state, action) => {
        state.products = action.payload;
      })
      .addCase(getProduct_bread.fulfilled, (state, action) => {
        state.products = action.payload;
      });
  },
});
export const { set_focusedProduct } = productSlice.actions;
export default productSlice.reducer;

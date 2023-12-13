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
export const sendOrder = createAsyncThunk(
  "product/sendOrder",
  async (
    {
      order_items,
      first_name,
      last_name,
      address_line_1,
      province,
      shipping_price,
    },
    thunkAPI
  ) => {
    try {
      const data = await ProductService.save_order(
        order_items,
        first_name,
        last_name,
        address_line_1,
        province,
        shipping_price
      );
      return data;
    } catch {
      return thunkAPI.rejectWithValue();
    }
  }
);
const productSlice = createSlice({
  name: "product",
  initialState: {
    products: [],
    focusedProduct: "icecream",
    streetOne: null,
    streetTwo: null,
    houseNumber: null,
    deliveryPrize: null,
    deliveryMunicipality: null,
    deliveryZone: null,
  },
  reducers: {
    set_focusedProduct: (state, action) => {
      state.focusedProduct = action.payload;
    },
    set_streetOne: (state, action) => {
      state.streetOne = action.payload;
    },
    set_streetTwo: (state, action) => {
      state.streetTwo = action.payload;
    },
    set_houseNumber: (state, action) => {
      state.houseNumber = action.payload;
    },
    set_deliveryPrize: (state, action) => {
      state.deliveryPrize = action.payload;
    },
    set_deliveryMunicipality: (state, action) => {
      state.deliveryMunicipality = action.payload;
    },
    set_deliveryZone: (state, action) => {
      state.deliveryZone = action.payload;
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
export const {
  set_focusedProduct,
  set_streetOne,
  set_streetTwo,
  set_houseNumber,
  set_deliveryPrize,
  set_deliveryMunicipality,
  set_deliveryZone,
} = productSlice.actions;
export default productSlice.reducer;

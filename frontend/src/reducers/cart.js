export const cartInitialState = JSON.parse(window.localStorage.getItem('cart')) || []

export const CART_ACTION_TYPE = {
    ADD_TO_CART: 'ADD_TO_CART',
    SUBTRACT_TO_CART: 'SUBTRACT_TO_CART',
    REMOVE_FROM_CART: 'REMOVE_FROM_CART',
    CLEAR_CART: 'CLEAR_CART'
}

export const updateLocalStorage = state => {
    window.localStorage.setItem('cart', JSON.stringify(state))
}

export const cartReducer = (state, action) => {

    const { type: actionType, payload: actionPayload } = action

    switch (actionType) {

        case CART_ACTION_TYPE.ADD_TO_CART: {
            const { id } = actionPayload
            const productInCartIndex = state.findIndex(item => item.id === id)

            if (productInCartIndex >= 0) {
                const newState = structuredClone(state)
                newState[productInCartIndex].count += 1
                updateLocalStorage(newState)
                return newState
            }

            const newState = [
                ...state,
                {
                    ...actionPayload, //product
                    count: 1
                }
            ]

            updateLocalStorage(newState)
            return newState
        }

        case CART_ACTION_TYPE.SUBTRACT_TO_CART: {
            const { id } = actionPayload;
            const productInCartIndex = state.findIndex(item => item.id === id);

            if (productInCartIndex >= 0) {
                const newState = structuredClone(state);
                newState[productInCartIndex].count -= 1;

                if (newState[productInCartIndex].count === 0) {
                    newState.splice(productInCartIndex, 1);
                }

                updateLocalStorage(newState);
                return newState;
            }

            return state;
        }

        case CART_ACTION_TYPE.REMOVE_FROM_CART: {
            const { id } = actionPayload
            const newState = state.filter(item => item.id !== id)
            updateLocalStorage(newState)
            return newState
        }

        case CART_ACTION_TYPE.CLEAR_CART: {
            updateLocalStorage([])
            return []
        }
    }

    return state
}
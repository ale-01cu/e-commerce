import "./loginform.css";
import { useState, useEffect } from "react";
import { useDispatch, useSelector } from "react-redux";
import { login } from "../../../redux/slices/authSlice";
import { clearMessage } from "../../../redux/slices/messageSlice";
import { Link, useNavigate } from "react-router-dom";
import { Toaster } from "sonner";
import { Formik, Field, Form, ErrorMessage } from "formik";
import * as Yup from "yup";

export function Login() {
  let navigate = useNavigate();
  const [loading, setLoading] = useState(false);

  const { isLoggedIn } = useSelector((state) => state.auth);
  const { message } = useSelector((state) => state.message);
  const dispatch = useDispatch();

  useEffect(() => {
    dispatch(clearMessage());
  }, [dispatch]);
  const initialValues = {
    loginname: "",
    password: "",
  };

  const validationSchema = Yup.object().shape({
    loginname: Yup.string().required("Ingresa un usuario válido"),
    password: Yup.string().required("Ingresa una contraseña"),
  });

  const handleSubmit = (formValue) => {
    const { loginname, password } = formValue;
    setLoading(true);
    dispatch(login({ loginname, password }))
      .unwrap()
      .then(() => {
        navigate("/");
      })
      .catch(() => {
        setLoading(false);
      });
  };

  return (
    <div className="login-form-container">
      <Toaster position="top-center" expand="true" richColors="true" />
      <h1>Login</h1>

      <div className="container-formik">
        <Formik
          initialValues={initialValues}
          validationSchema={validationSchema}
          onSubmit={handleSubmit}
        >
          <Form>
            <div className="box-input">
              <Field
                type="email"
                name="loginname"
                id="loginname"
                placeholder="Escriba su email"
              />
              <span>Email</span>
            </div>

            <ErrorMessage name="loginname" component="div" className="login-error" />

            <div className="box-input">
              <Field
                type="password"
                name="password"
                id="password"
                placeholder="Escriba su contraseña"
              />
              <span>Contraseña</span>
            </div>

            <ErrorMessage name="password" component="div" className="login-error" />

            <Link to="/register" id="forgot-password">
              <span>Crear cuenta nueva</span>
            </Link>

            <div className="login-button-container">
              <div id="login" className="login-button-submit">
                <button
                  className={loading ? "next" : "login-button"}
                  type="submit"
                  disabled={loading}
                >
                  Iniciar sesión
                </button>
              </div>

              <span
                id="loadingLogin"
                className={loading ? "box box-active" : "box next"}
              >
                <p>adasdasd</p>
              </span>
            </div>
          </Form>
        </Formik>
      </div>

      {message && (
        <div className="" style={{ marginTop: 30, marginLeft: 55 }}>
          <div className="" role="alert">
            {message}
          </div>
        </div>
      )}
    </div>
  );
}

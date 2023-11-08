import "./registerform.css";
import { useState, useEffect } from "react";
import { useDispatch, useSelector } from "react-redux";
import { register } from "../../../redux/slices/authSlice";
import { clearMessage } from "../../../redux/slices/messageSlice";
import { Link, useNavigate } from "react-router-dom";
import { Formik, Field, Form, ErrorMessage } from "formik";
import * as Yup from "yup";
export function Register() {
  let navigate = useNavigate();
  const [loading, setLoading] = useState(false);
  const [successful, setSuccessful] = useState(false);
  const { isLoggedIn } = useSelector((state) => state.auth);
  const { message } = useSelector((state) => state.message);
  const dispatch = useDispatch();

  useEffect(() => {
    dispatch(clearMessage());
  }, [dispatch]);
  const initialValues = {
    first_name: "",
    lasttname: "",
    email: "",
    password: "",
    re_password: "",
    phone_number: "",
    birthdate: "",
  };
  const regexp = new RegExp(
    /^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[^a-zA-Z\d]).{8,}$/
  );
  const regext = new RegExp(/\+53\d{8}/);
  const validationSchema = Yup.object().shape({
    first_name: Yup.string()
      .test(
        "len",
        "El usuario debe tener entre 3 y 20 caracteres",
        (val) =>
          val && val.toString().length >= 3 && val.toString().length <= 20
      )
      .required("Ingresa un usuario válido"),
    last_name: Yup.string().required("Rellena este campo"),
    email: Yup.string()
      .email("El correo es incorrecto")
      .required("Ingresa un correo válido"),
    password: Yup.string()
      .test(
        "len",
        "La contraseña debe tener al menos 6 caracteres y no más de 40",
        (val) =>
          val && val.toString().length >= 6 && val.toString().length <= 40
      )
      .matches(regexp, "Contraseña débil")
      .required("Ingresa una contraseña válida"),
    re_password: Yup.string()
      .required("Vuelva a insertar su contraseña")
      .oneOf([Yup.ref("password"), null], "Las contraseñas no coinciden"),
    birthdate: Yup.date().required("ingresa tu cumpleaños"),
    phone_number: Yup.string()
      .max(11, "Telefono incorrecto")
      .matches(regext, "Telefono incorrecto"),
  });
  const handleRegister = (formValue) => {
    const {
      first_name,
      last_name,
      email,
      password,
      re_password,
      phone_number,
      birthdate,
    } = formValue;
    setSuccessful(false);
    dispatch(
      register({
        first_name,
        last_name,
        email,
        password,
        re_password,
        phone_number,
        birthdate,
      })
    )
      .unwrap()
      .then(() => {
        setSuccessful(true);
      })
      .catch(() => {
        setSuccessful(false);
      });
  };
  return (
    <div className="register-container-form">
      <h1>Registrarte</h1>
      <Formik
        initialValues={initialValues}
        validationSchema={validationSchema}
        onSubmit={handleRegister}
      >
        <Form className="form-register-container" action="">
          <div className="box-input">
            <label htmlFor="first_name">Nombre</label>
            <Field name="first_name">
              {({ field, form, meta }) => (
                <div>
                  <input
                    type="text"
                    className={meta.touched && meta.error && "field_error"}
                    id="register_name"
                    placeholder="Escriba su nombre"
                    {...field}
                  ></input>
                </div>
              )}
            </Field>
            <ErrorMessage
              name="first_name"
              component="div"
              className="alert-danger"
            />
          </div>

          <div className="box-input">
            <label htmlFor="last_name">Apellidos</label>
            <Field name="last_name">
              {({ field, form, meta }) => (
                <div>
                  <input
                    type="text"
                    className={meta.touched && meta.error && "field_error"}
                    id="register_lastname"
                    placeholder="Escriba su nombre"
                    {...field}
                  ></input>
                </div>
              )}
            </Field>
            <ErrorMessage
              name="last_name"
              component="div"
              className="alert-danger"
            />
          </div>

          <div className="box-input">
            <label htmlFor="phone_number">Teléfono</label>
            <Field
              name="phone_number"
            // maxLength={11}
            >
              {({ field, form, meta }) => (
                <div>
                  <input
                    type="tel"
                    className={meta.touched && meta.error && "field_error"}
                    id="register_phonenumber"
                    placeholder="Ej: +5351234567"
                    {...field}
                  ></input>
                </div>
              )}
            </Field>
            <ErrorMessage
              name="phone_number"
              component="div"
              className="alert-danger"
            />
          </div>

          <div className="box-input">
            <label htmlFor="password">Contraseña</label>
            <Field
              name="password"

            //pattern="^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[^\da-zA-Z]).{8,}$"
            >
              {({ field, form, meta }) => (
                <div>
                  <input
                    type="password"
                    className={meta.touched && meta.error && "field_error"}
                    id="register_password"
                    placeholder="Contraseña"
                    {...field}
                  ></input>
                </div>
              )}
            </Field>
            <ErrorMessage
              name="password"
              component="div"
              className="alert-danger"
            />
          </div>

          <div className="box-input">
            <label htmlFor="re_password">Confirmar contraseña</label>
            <Field name="re_password">
              {({ field, form, meta }) => (
                <div>
                  <input
                    type="password"
                    className={meta.touched && meta.error && "field_error"}
                    id="register_confir_password"
                    placeholder="Confirmar contraseña"
                    {...field}
                  ></input>
                  <svg xmlns="http://www.w3.org/2000/svg" fill="none" width={30} height={30} viewBox="0 0 24 24" strokeWidth={1.5} stroke="currentColor" className="pass">
                    <path strokeLinecap="round" strokeLinejoin="round" d="M11.25 9l-3 3m0 0l3 3m-3-3h7.5M21 12a9 9 0 11-18 0 9 9 0 0118 0z" />
                  </svg>
                </div>
              )}
            </Field>
            <ErrorMessage
              name="re_password"
              component="div"
              className="alert-danger"
            />
          </div>

          <div className="box-input">
            <label htmlFor="email">Email</label>
            <Field name="email">
              {({ field, form, meta }) => (
                <div>
                  <input
                    type="email"
                    className={meta.touched && meta.error && "field_error"}
                    id="register_email"
                    placeholder="Ej: hi@gmail.com"
                    //pattern="[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"
                    {...field}
                  ></input>
                </div>
              )}
            </Field>
            <ErrorMessage
              name="email"
              component="div"
              className="alert-danger"
            />
          </div>

          <div className="box-input">
            <label htmlFor="date">Fecha de nacimiento</label>
            <Field name="birthdate">
              {({ field, form, meta }) => (
                <div>
                  <input
                    className={meta.touched && meta.error && "field_error"}
                    type="date"
                    id="register_birthdate"
                    {...field}
                  ></input>
                </div>
              )}
            </Field>
            <ErrorMessage
              name="birthdate"
              component="div"
              className="alert-danger"
            />
          </div>

          <Link to="/login" id="forgot-password">
            <span className="">Ya tengo cuenta</span>
          </Link>

          <div className="button-container">
            <div className="">
              <button type="submit">Crear cuenta</button>
              {/* Aqui va el envio al server para crear cuenta  */}
            </div>
          </div>
        </Form>
      </Formik>
      {message && (
        <div className="events_register">
          <div className={successful ? "success" : "danger"}>{message}</div>
        </div>
      )}
    </div>
  );
}

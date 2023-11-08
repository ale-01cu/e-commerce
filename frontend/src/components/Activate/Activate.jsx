import { useParams } from "react-router-dom";
import { useDispatch } from "react-redux";
import { activate } from "../../redux/slices/authSlice";
import { Link, useNavigate } from "react-router-dom";
import { useState } from "react";
export default function Activate() {
  const [isActivated, setisActivated] = useState(false);
  const [loading, setLoading] = useState(false);
  const dispatch = useDispatch();
  const params = useParams();
  const navigate = useNavigate();
  const activate_account = () => {
    const uid = params.uid;
    const token = params.token;
    setLoading(true);
    dispatch(activate({ uid, token }))
      .unwrap()
      .then(() => {
        setisActivated(true);
        navigate("/");
      })
      .catch(() => {
        setLoading(false);
      });
  };

  return (
    <>
      <button onClick={activate_account}>Activar cuenta</button>
    </>
  );
}

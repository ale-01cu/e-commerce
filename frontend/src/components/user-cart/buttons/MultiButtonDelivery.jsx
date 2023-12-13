import React, { useState, useEffect } from "react";
import jsonData from "../../../assets/js/jsondata.json";
import "./buttondelivery.css";
import { useDispatch } from "react-redux";
import {
  set_deliveryMunicipality,
  set_deliveryPrize,
  set_deliveryZone,
} from "../../../redux/slices/productSlice";

// hemos utilizado useEffect para cargar los datos del archivo JSON en el
// estado una vez que el componente se haya montado.Luego, en el primer select,
// hemos mapeado los elementos de municipios para crear las opciones.Al seleccionar
//  un municipio, llamamos a la función handleMunicipioChange para filtrar las zonas
//  correspondientes y almacenarlas en el estado zonas.Finalmente, en el segundo select,
//  mapeamos los elementos de zonas para crear las opciones.

export const MultiButtonDelivery = ({ actualizarTarifa }) => {
  const [municipios, setMunicipios] = useState([]);
  const [zonas, setZonas] = useState([]);
  const dispatch = useDispatch();
  const [selectedMunicipio, setSelectedMunicipio] = useState("");
  const [selectedZona, setSelectedZona] = useState("");
  const [newtarifa, setNewTarifa] = useState(0);

  useEffect(() => {
    setMunicipios(jsonData.municipios);
  }, []);

  // Cambio de municipio y reinicio de tarifas en 0 junto a al cambio de zona
  const handleMunicipioChange = (event) => {
    const selectedMunicipio = event.target.value;
    const selectedMunicipioData = municipios.find(
      (municipio) => municipio.municipio === selectedMunicipio
    );

    setZonas(selectedMunicipioData.zonas);
    setSelectedMunicipio(selectedMunicipio);
    setSelectedZona("");
    setNewTarifa(0);
    actualizarTarifa(0);
  };

  // Obtencion del valor de la tarifa y actualizacion de los estados a traves de la llamada a la funcion
  const handleZonaChange = (event) => {
    const selectedZona = event.target.value;
    setSelectedZona(selectedZona);

    const selectedMunicipioData = municipios.find(
      (municipio) => municipio.municipio === selectedMunicipio
    );
    const selectedZonaData = selectedMunicipioData.zonas.find(
      (zona) => zona.zona === selectedZona
    );
    dispatch(set_deliveryMunicipality(selectedMunicipioData.municipio));
    dispatch(set_deliveryZone(selectedZonaData.zona));
    const tarifaZonaSeleccionada = selectedZonaData.tarifa;
    setNewTarifa(tarifaZonaSeleccionada);
    actualizarTarifa(tarifaZonaSeleccionada);
    dispatch(set_deliveryPrize(tarifaZonaSeleccionada));
  };

  return (
    <>
      <select className="buttondelivery" onChange={handleMunicipioChange}>
        <option value="">Municipio</option>
        {municipios.map((municipio, index) => (
          <option key={index} value={municipio.municipio}>
            {municipio.municipio}
          </option>
        ))}
      </select>

      <select
        className="buttondelivery"
        onChange={handleZonaChange}
        value={selectedZona}
      >
        <option value="">Zona</option>
        {zonas.map((zona, index) => (
          <option key={index} value={zona.zona}>
            {zona.zona}
          </option>
        ))}
      </select>
    </>
  );
};

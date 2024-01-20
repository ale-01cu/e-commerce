import { useEffect, useState } from "react";
import "./category.css";

export function Category({handleClickI,handleClickB}) {
  const [ categorys, setCategorys ] = useState([])

  useEffect(() => {
    fetch('http://localhost:8000/api/categorys/')
      .then(res => res.json())
      .then(data => setCategorys(data))
      .catch(error => console.log(error))
  }, [])
  
  return (
    <section className="section-category">
      {
        categorys.map(category => (
          <div key={category.id} className="section-category__icecream">
            <img
              src={category.photo}
              alt="Section de Helados Magic, podrás encontrar todos los sabores que más te gustan !"
              onClick={handleClickI}
            />
            <p>{category.name}</p>
          </div>
        ))
      }
    </section>
  );
}

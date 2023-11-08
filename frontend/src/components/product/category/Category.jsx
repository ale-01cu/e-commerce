import "./category.css";

export function Category({handleClickI,handleClickB}) {
  
  return (
    <>
      <section className="section-category">
        <div className="section-category__icecream">
          <img
            src="../src/assets/img/Diseño_sin_título__4_-removebg-preview.png"
            alt="Section de Helados Magic, podrás encontrar todos los sabores que más te gustan !"
            onClick={handleClickI}
          />
          <p>Helados</p>
        </div>
        <div className="section-category__bread">
          <img
            src="../src/assets/img/Diseño_sin_título__5_-removebg-preview.png"
            alt="Section de Panes Magic, podrás encontrar variedades de panes al gusto !"
            onClick={handleClickB}
          />
          <p>Panes</p>
        </div>
      </section>
    </>
  );
}

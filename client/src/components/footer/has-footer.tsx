import './has-footer.scss';
import informationUri from '../../assets/information.svg';

const HasFooter = ({ children }: any) => {
  return (
    <div className="wrapper">
      <div className="content-wrapper">{children}</div>
      <footer>
        <div className="image-text">
          <img alt="more information logo" src={informationUri} />
          <span>András Schmelczer & Leonardo Pohl</span>
        </div>
      </footer>
    </div>
  );
};

export default HasFooter;

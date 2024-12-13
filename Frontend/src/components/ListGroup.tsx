import { Fragment } from "react/jsx-runtime";
import { MouseEvent, useState } from "react";

interface Prpos {
    items: string[];
    heading: string;
}
// props: Prpos or 
function ListGroup({ items, heading }: Prpos) {
  

  //<Fragment> // or you can use empty brackets
  // <>
  //   <h1>List</h1>
  //   <ul className="list-group">
  //     <li className="list-group-item">An item</li>
  //     <li className="list-group-item">A second item</li>
  //     <li className="list-group-item">A third item</li>
  //     <li className="list-group-item">A fourth item</li>
  //     <li className="list-group-item">And a fifth one</li>
  //   </ul>
  // </>
  //</Fragment>
  
  const message = items.length === 0 ? <p>There are no items!</p> : null;
  
//   const arr = useState(-1);
//   arr[0]; // value
//   arr[1]; // function to set the value
const [selectedIndex, setSelectedIndex] = useState(-1);
const [name, setName] = useState('');
  return ( 
    <>
      <h1>{heading}</h1>
      {/* {items.length == 0 ? <p>There are no items!</p> : null} */}
      {items.length === 0 && <p>There are no items!</p>}
      {/* That is because in javascript true && b = b and false && b = false*/}
      {message}
      <ul className="list-group">
        {items.map((item, index) => (
          <li
            className={
              selectedIndex === index
                ? "list-group-item active"
                : "list-group-item"
            } // conditional rendering
            key={item}
            onClick={() => { setSelectedIndex(index);}} // event handler
          >
            {item}
          </li> // required for react to keep track of the items
        ))}
      </ul>
    </>
  );
}

// returning multiple tags
// you cant do that in react

export default ListGroup;

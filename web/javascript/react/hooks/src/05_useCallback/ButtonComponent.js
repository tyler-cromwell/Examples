import React from 'react'


function ButtonComponent({ handler, children }) {
  console.log('Rendering button: ', children)
  return (
    <button onClick={handler}>
      {children}
    </button>
  )
}


export default React.memo(ButtonComponent)

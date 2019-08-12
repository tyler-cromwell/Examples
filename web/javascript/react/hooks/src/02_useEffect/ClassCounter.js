import React, { Component } from 'react'

class ClassCounter extends Component {
  constructor(props) {
    super(props)
    this.state = {
      count: 0,
      name: ''
    }
  }

  componentDidMount() {
    document.title = `Class 02: clicked ${this.state.count} times`
  }

  componentDidUpdate(prevProps, prevState) {
    console.log('[Class] componentDidUpdate')
    if (prevState.count !== this.state.count) {
      console.log('[Class] Updating document title...')
      document.title = `Class 02: clicked ${this.state.count} times`
    }
  }

  incrementCount = () => {
    this.setState({
      count: this.state.count + 1
    })
  }

  updateName = (e) => {
    this.setState({
      name: e.target.value
    })
  }

  render() {
    return (
      <div>
        Class Count: {this.state.count}
        <button onClick={this.incrementCount}>Increment</button>
        <input type="text" value={this.state.name} onChange={this.updateName}/>
      </div>
    )
  }
}

export default ClassCounter

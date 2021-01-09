/* App.js */
import { Navbar, Button, Nav, Form } from "react-bootstrap";
// import { useState } from "react";
var React = require("react");
var Component = React.Component;
var CanvasJSReact = require("./canvasjs.react").default;
var CanvasJS = CanvasJSReact.CanvasJS;
var CanvasJSChart = CanvasJSReact.CanvasJSChart;
var datapoint_amazon = [];
var datapoint_flipkart = [];
// var [datapoint_amazon, setdatapoint_amazon] = useState([]);
// var [datapoint_flipkart,setdatapoint_flipkart]=useState([]);

class Home extends Component {
  render() {
    const options = {
      animationEnabled: true,
      title: {
        text: "Price Comparison",
      },
      axisY: {
        title: "Price in Rs",
      },
      toolTip: {
        shared: true,
      },
      data: [
        {
          name: "Amazon",
          showInLegend: true,
          type: "spline",
          dataPoints: datapoint_amazon,
        },
        {
          type: "spline",
          name: "Flipkart",
          showInLegend: true,
          dataPoints: datapoint_flipkart,
        },
      ],
    };
    return (
      <div className="home-page">
        <Navbar className="color-nav" variant="dark">
          <Navbar.Brand href="#home">Navbar</Navbar.Brand>
          <Nav className="mr-auto">
            <Nav.Link href="#home">Home</Nav.Link>
            <Nav.Link href="#features">About</Nav.Link>
          </Nav>
        </Navbar>
        <br />

        <div className="product-form">
          <Form>
            <Form.Group controlId="formBasicEmail">
              <Form.Label>Enter the Amazon URL of product</Form.Label>
              <Form.Control placeholder="Amazon URL" />
            </Form.Group>
            <Form.Group controlId="formBasicEmail">
              <Form.Label>Enter the Flipkart URL of product</Form.Label>
              <Form.Control placeholder="Flipkart URL" />
            </Form.Group>

            <Button variant="primary" type="submit">
              Submit
            </Button>
          </Form>
        </div>
        <div className="graph">
          <div>
            <CanvasJSChart
              options={options}
              onRef={(ref) => (this.chart = ref)}
            />
          </div>
        </div>
      </div>
    );
  }

  componentDidMount() {
    var chart = this.chart;
    console.log(chart);
    fetch("https://api.npoint.io/2f035e5c441af33d50a7")
      .then(function (response) {
        return response.json();
      })
      .then(function (data) {
        console.log(data);
        for (var i = 0; i < data.websites.amazon.length; i++) {
          let time = data.datetime[i];
          let ftime = new Date(time);
          ftime =
            String(ftime).slice(4, 10) + " " + String(ftime).slice(16, 21);
          datapoint_amazon.push({
            y: data.websites.amazon[i],
            label: ftime,
          });
          datapoint_flipkart.push({
            y: data.websites.flipkart[i],
            label: ftime,
          });
        }
        console.log(datapoint_amazon);
        console.log(datapoint_flipkart);
        chart.render();
      });
  }
}

export default Home;

import { Navbar, Button, Nav, Form, FormControl } from "react-bootstrap";
var React = require("react");
var Component = React.Component;
var CanvasJSReact = require("./canvasjs.react").default;
var CanvasJS = CanvasJSReact.CanvasJS;
var CanvasJSChart = CanvasJSReact.CanvasJSChart;
function Home() {
  const options = {
    animationEnabled: true,
    title: {
      text: "Price Comparison",
    },
    axisY: {
      title: "Number of Customers",
    },
    toolTip: {
      shared: true,
    },
    data: [
      {
        type: "spline",
        name: "Amazon",
        showInLegend: true,
        dataPoints: [
          { y: 155, label: "Jan" },
          { y: 150, label: "Feb" },
          { y: 152, label: "Mar" },
          { y: 148, label: "Apr" },
          { y: 142, label: "May" },
          { y: 150, label: "Jun" },
          { y: 146, label: "Jul" },
          { y: 149, label: "Aug" },
          { y: 153, label: "Sept" },
          { y: 158, label: "Oct" },
          { y: 154, label: "Nov" },
          { y: 150, label: "Dec" },
        ],
      },
      {
        type: "spline",
        name: "Flipkart",
        showInLegend: true,
        dataPoints: [
          { y: 172, label: "Jan" },
          { y: 173, label: "Feb" },
          { y: 175, label: "Mar" },
          { y: 172, label: "Apr" },
          { y: 162, label: "May" },
          { y: 165, label: "Jun" },
          { y: 172, label: "Jul" },
          { y: 168, label: "Aug" },
          { y: 175, label: "Sept" },
          { y: 170, label: "Oct" },
          { y: 165, label: "Nov" },
          { y: 169, label: "Dec" },
        ],
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
            <Form.Label>Enter the amazon URL of product</Form.Label>
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
            /* onRef={ref => this.chart = ref} */
          />
          {/*You can get reference to the chart instance as shown above using onRef. This allows you to access all chart properties and methods*/}
        </div>
      </div>
    </div>
  );
}

export default Home;

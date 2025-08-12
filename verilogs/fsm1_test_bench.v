module fsm1_test_bench();

reg clk, rst, timer_done, pedestrian_request;
wire main_green, side_green, warning;

fsm1 test_fsm(clk, rst, timer_done, pedestrian_request, main_green, side_green, warning);

initial begin
  timer_done = 0;
  pedestrian_request = 0;
end

initial begin
  #10 rst=1;
  #10 rst=0;
  #10
    clk=0;
    timer_done = 1;
    pedestrian_request = 1;
  #10  clk=1;
  #10
    clk=0;
    timer_done = 1;
    pedestrian_request = 0;
  #10  clk=1;
  #10
    clk=0;
    timer_done = 0;
    pedestrian_request = 1;
  #10  clk=1;
  #10
    clk=0;
    timer_done = 1;
    pedestrian_request = 0;
  #10  clk=1;
  #10
    clk=0;
    timer_done = 1;
    pedestrian_request = 0;
  #10  clk=1;
  
  #10 rst=1;
  #10 rst=0;
  #10
    clk=0;
    timer_done = 1;
    pedestrian_request = 1;
  #10  clk=1;
  #10
    clk=0;
    timer_done = 1;
    pedestrian_request = 0;
  #10  clk=1;
  #10
    clk=0;
    timer_done = 0;
    pedestrian_request = 1;
  #10  clk=1;
  #10
    clk=0;
    timer_done = 1;
    pedestrian_request = 0;
  #10  clk=1;
  #10
    clk=0;
    timer_done = 0;
    pedestrian_request = 0;
  #10  clk=1;
  
  #10 rst=1;
  #10 rst=0;
  #10
    clk=0;
    timer_done = 1;
    pedestrian_request = 1;
  #10  clk=1;
  #10
    clk=0;
    timer_done = 1;
    pedestrian_request = 0;
  #10  clk=1;
  #10
    clk=0;
    timer_done = 0;
    pedestrian_request = 1;
  #10  clk=1;
  #10
    clk=0;
    timer_done = 0;
    pedestrian_request = 0;
  #10  clk=1;
  
  #10 rst=1;
  #10 rst=0;
  #10
    clk=0;
    timer_done = 1;
    pedestrian_request = 1;
  #10  clk=1;
  #10
    clk=0;
    timer_done = 1;
    pedestrian_request = 0;
  #10  clk=1;
  #10
    clk=0;
    timer_done = 1;
    pedestrian_request = 0;
  #10  clk=1;
  
  #10 rst=1;
  #10 rst=0;
  #10
    clk=0;
    timer_done = 1;
    pedestrian_request = 1;
  #10  clk=1;
  #10
    clk=0;
    timer_done = 1;
    pedestrian_request = 0;
  #10  clk=1;
  #10
    clk=0;
    timer_done = 0;
    pedestrian_request = 0;
  #10  clk=1;
  
  #10 rst=1;
  #10 rst=0;
  #10
    clk=0;
    timer_done = 1;
    pedestrian_request = 1;
  #10  clk=1;
  #10
    clk=0;
    timer_done = 0;
    pedestrian_request = 0;
  #10  clk=1;
  
  #10 rst=1;
  #10 rst=0;
  #10
    clk=0;
    timer_done = 1;
    pedestrian_request = 0;
  #10  clk=1;
  
  #10 rst=1;
  #10 rst=0;
  #10
    clk=0;
    timer_done = 0;
    pedestrian_request = 0;
  #10  clk=1;
  
  
end

endmodule
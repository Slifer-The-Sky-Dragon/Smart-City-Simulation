module fsm2_test_bench();

reg clk, rst, pin_correct, door_closed, intruder_detected;
wire lock_state, alarm_state;

fsm2 test_fsm(clk, rst, pin_correct, door_closed, intruder_detected, lock_state, alarm_state);

initial begin
  pin_correct = 0;
  door_closed = 0;
  intruder_detected = 0;
end

initial begin
  #10 rst=1;
  #10 rst=0;
  #10
    clk=0;
    pin_correct = 1;
    door_closed = 1;
    intruder_detected = 0;
  #10  clk=1;
  #10
    clk=0;
    pin_correct = 0;
    door_closed = 0;
    intruder_detected = 0;
  #10  clk=1;
  
  #10 rst=1;
  #10 rst=0;
  #10
    clk=0;
    pin_correct = 1;
    door_closed = 1;
    intruder_detected = 0;
  #10  clk=1;
  #10
    clk=0;
    pin_correct = 0;
    door_closed = 0;
    intruder_detected = 1;
  #10  clk=1;
  #10
    clk=0;
    pin_correct = 1;
    door_closed = 0;
    intruder_detected = 0;
  #10  clk=1;
  
  #10 rst=1;
  #10 rst=0;
  #10
    clk=0;
    pin_correct = 1;
    door_closed = 1;
    intruder_detected = 0;
  #10  clk=1;
  #10
    clk=0;
    pin_correct = 0;
    door_closed = 0;
    intruder_detected = 1;
  #10  clk=1;
  #10
    clk=0;
    pin_correct = 0;
    door_closed = 0;
    intruder_detected = 0;
  #10  clk=1;
  
  #10 rst=1;
  #10 rst=0;
  #10
    clk=0;
    pin_correct = 0;
    door_closed = 0;
    intruder_detected = 1;
  #10  clk=1;
  
  
end

endmodule
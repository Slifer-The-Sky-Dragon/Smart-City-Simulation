module fsm3_test_bench();

reg clk, rst, call_ground, call_floor1, call_floor2, call_floor3, floor_sensor1, floor_sensor2, floor_sensor3, emergency_stop;
wire moving, idle, alarm;

fsm3 test_fsm(clk, rst, call_ground, call_floor1, call_floor2, call_floor3, floor_sensor1, floor_sensor2, floor_sensor3, emergency_stop, moving, idle, alarm);

initial begin
  call_ground = 0;
  call_floor1 = 0;
  call_floor2 = 0;
  call_floor3 = 0;
  floor_sensor1 = 0;
  floor_sensor2 = 0;
  floor_sensor3 = 0;
  emergency_stop = 0;
end

initial begin
  #10 rst=1;
  #10 rst=0;
  #10
    clk=0;
    call_ground = 0;
    call_floor1 = 1;
    call_floor2 = 0;
    call_floor3 = 0;
    floor_sensor1 = 0;
    floor_sensor2 = 0;
    floor_sensor3 = 0;
    emergency_stop = 0;
  #10  clk=1;
  #10
    clk=0;
    call_ground = 0;
    call_floor1 = 0;
    call_floor2 = 0;
    call_floor3 = 0;
    floor_sensor1 = 1;
    floor_sensor2 = 0;
    floor_sensor3 = 0;
    emergency_stop = 0;
  #10  clk=1;
  #10
    clk=0;
    call_ground = 1;
    call_floor1 = 0;
    call_floor2 = 0;
    call_floor3 = 0;
    floor_sensor1 = 0;
    floor_sensor2 = 0;
    floor_sensor3 = 0;
    emergency_stop = 0;
  #10  clk=1;
  #10
    clk=0;
    call_ground = 0;
    call_floor1 = 0;
    call_floor2 = 0;
    call_floor3 = 0;
    floor_sensor1 = 1;
    floor_sensor2 = 0;
    floor_sensor3 = 0;
    emergency_stop = 0;
  #10  clk=1;
  
  #10 rst=1;
  #10 rst=0;
  #10
    clk=0;
    call_ground = 0;
    call_floor1 = 1;
    call_floor2 = 0;
    call_floor3 = 0;
    floor_sensor1 = 0;
    floor_sensor2 = 0;
    floor_sensor3 = 0;
    emergency_stop = 0;
  #10  clk=1;
  #10
    clk=0;
    call_ground = 0;
    call_floor1 = 0;
    call_floor2 = 0;
    call_floor3 = 0;
    floor_sensor1 = 1;
    floor_sensor2 = 0;
    floor_sensor3 = 0;
    emergency_stop = 0;
  #10  clk=1;
  #10
    clk=0;
    call_ground = 1;
    call_floor1 = 0;
    call_floor2 = 0;
    call_floor3 = 0;
    floor_sensor1 = 0;
    floor_sensor2 = 0;
    floor_sensor3 = 0;
    emergency_stop = 0;
  #10  clk=1;
  #10
    clk=0;
    call_ground = 0;
    call_floor1 = 0;
    call_floor2 = 0;
    call_floor3 = 0;
    floor_sensor1 = 0;
    floor_sensor2 = 0;
    floor_sensor3 = 0;
    emergency_stop = 1;
  #10  clk=1;
  #10
    clk=0;
    call_ground = 1;
    call_floor1 = 0;
    call_floor2 = 0;
    call_floor3 = 0;
    floor_sensor1 = 0;
    floor_sensor2 = 0;
    floor_sensor3 = 0;
    emergency_stop = 0;
  #10  clk=1;
  
  #10 rst=1;
  #10 rst=0;
  #10
    clk=0;
    call_ground = 0;
    call_floor1 = 1;
    call_floor2 = 0;
    call_floor3 = 0;
    floor_sensor1 = 0;
    floor_sensor2 = 0;
    floor_sensor3 = 0;
    emergency_stop = 0;
  #10  clk=1;
  #10
    clk=0;
    call_ground = 0;
    call_floor1 = 0;
    call_floor2 = 0;
    call_floor3 = 0;
    floor_sensor1 = 1;
    floor_sensor2 = 0;
    floor_sensor3 = 0;
    emergency_stop = 0;
  #10  clk=1;
  #10
    clk=0;
    call_ground = 1;
    call_floor1 = 0;
    call_floor2 = 0;
    call_floor3 = 0;
    floor_sensor1 = 0;
    floor_sensor2 = 0;
    floor_sensor3 = 0;
    emergency_stop = 0;
  #10  clk=1;
  #10
    clk=0;
    call_ground = 0;
    call_floor1 = 0;
    call_floor2 = 0;
    call_floor3 = 0;
    floor_sensor1 = 0;
    floor_sensor2 = 0;
    floor_sensor3 = 0;
    emergency_stop = 1;
  #10  clk=1;
  #10
    clk=0;
    call_ground = 0;
    call_floor1 = 0;
    call_floor2 = 0;
    call_floor3 = 0;
    floor_sensor1 = 0;
    floor_sensor2 = 0;
    floor_sensor3 = 0;
    emergency_stop = 0;
  #10  clk=1;
  
  #10 rst=1;
  #10 rst=0;
  #10
    clk=0;
    call_ground = 0;
    call_floor1 = 1;
    call_floor2 = 0;
    call_floor3 = 0;
    floor_sensor1 = 0;
    floor_sensor2 = 0;
    floor_sensor3 = 0;
    emergency_stop = 0;
  #10  clk=1;
  #10
    clk=0;
    call_ground = 0;
    call_floor1 = 0;
    call_floor2 = 0;
    call_floor3 = 0;
    floor_sensor1 = 1;
    floor_sensor2 = 0;
    floor_sensor3 = 0;
    emergency_stop = 0;
  #10  clk=1;
  #10
    clk=0;
    call_ground = 0;
    call_floor1 = 0;
    call_floor2 = 1;
    call_floor3 = 0;
    floor_sensor1 = 0;
    floor_sensor2 = 0;
    floor_sensor3 = 0;
    emergency_stop = 0;
  #10  clk=1;
  #10
    clk=0;
    call_ground = 0;
    call_floor1 = 0;
    call_floor2 = 0;
    call_floor3 = 0;
    floor_sensor1 = 0;
    floor_sensor2 = 1;
    floor_sensor3 = 0;
    emergency_stop = 0;
  #10  clk=1;
  #10
    clk=0;
    call_ground = 1;
    call_floor1 = 0;
    call_floor2 = 0;
    call_floor3 = 0;
    floor_sensor1 = 0;
    floor_sensor2 = 0;
    floor_sensor3 = 0;
    emergency_stop = 0;
  #10  clk=1;
  #10
    clk=0;
    call_ground = 0;
    call_floor1 = 0;
    call_floor2 = 0;
    call_floor3 = 0;
    floor_sensor1 = 0;
    floor_sensor2 = 1;
    floor_sensor3 = 0;
    emergency_stop = 0;
  #10  clk=1;
  
  #10 rst=1;
  #10 rst=0;
  #10
    clk=0;
    call_ground = 0;
    call_floor1 = 1;
    call_floor2 = 0;
    call_floor3 = 0;
    floor_sensor1 = 0;
    floor_sensor2 = 0;
    floor_sensor3 = 0;
    emergency_stop = 0;
  #10  clk=1;
  #10
    clk=0;
    call_ground = 0;
    call_floor1 = 0;
    call_floor2 = 0;
    call_floor3 = 0;
    floor_sensor1 = 1;
    floor_sensor2 = 0;
    floor_sensor3 = 0;
    emergency_stop = 0;
  #10  clk=1;
  #10
    clk=0;
    call_ground = 0;
    call_floor1 = 0;
    call_floor2 = 1;
    call_floor3 = 0;
    floor_sensor1 = 0;
    floor_sensor2 = 0;
    floor_sensor3 = 0;
    emergency_stop = 0;
  #10  clk=1;
  #10
    clk=0;
    call_ground = 0;
    call_floor1 = 0;
    call_floor2 = 0;
    call_floor3 = 0;
    floor_sensor1 = 0;
    floor_sensor2 = 1;
    floor_sensor3 = 0;
    emergency_stop = 0;
  #10  clk=1;
  #10
    clk=0;
    call_ground = 1;
    call_floor1 = 0;
    call_floor2 = 0;
    call_floor3 = 0;
    floor_sensor1 = 0;
    floor_sensor2 = 0;
    floor_sensor3 = 0;
    emergency_stop = 0;
  #10  clk=1;
  #10
    clk=0;
    call_ground = 0;
    call_floor1 = 0;
    call_floor2 = 0;
    call_floor3 = 0;
    floor_sensor1 = 0;
    floor_sensor2 = 0;
    floor_sensor3 = 0;
    emergency_stop = 1;
  #10  clk=1;
  
  #10 rst=1;
  #10 rst=0;
  #10
    clk=0;
    call_ground = 0;
    call_floor1 = 1;
    call_floor2 = 0;
    call_floor3 = 0;
    floor_sensor1 = 0;
    floor_sensor2 = 0;
    floor_sensor3 = 0;
    emergency_stop = 0;
  #10  clk=1;
  #10
    clk=0;
    call_ground = 0;
    call_floor1 = 0;
    call_floor2 = 0;
    call_floor3 = 0;
    floor_sensor1 = 1;
    floor_sensor2 = 0;
    floor_sensor3 = 0;
    emergency_stop = 0;
  #10  clk=1;
  #10
    clk=0;
    call_ground = 0;
    call_floor1 = 0;
    call_floor2 = 1;
    call_floor3 = 0;
    floor_sensor1 = 0;
    floor_sensor2 = 0;
    floor_sensor3 = 0;
    emergency_stop = 0;
  #10  clk=1;
  #10
    clk=0;
    call_ground = 0;
    call_floor1 = 0;
    call_floor2 = 0;
    call_floor3 = 0;
    floor_sensor1 = 0;
    floor_sensor2 = 1;
    floor_sensor3 = 0;
    emergency_stop = 0;
  #10  clk=1;
  #10
    clk=0;
    call_ground = 0;
    call_floor1 = 1;
    call_floor2 = 0;
    call_floor3 = 0;
    floor_sensor1 = 0;
    floor_sensor2 = 0;
    floor_sensor3 = 0;
    emergency_stop = 0;
  #10  clk=1;
  
  #10 rst=1;
  #10 rst=0;
  #10
    clk=0;
    call_ground = 0;
    call_floor1 = 1;
    call_floor2 = 0;
    call_floor3 = 0;
    floor_sensor1 = 0;
    floor_sensor2 = 0;
    floor_sensor3 = 0;
    emergency_stop = 0;
  #10  clk=1;
  #10
    clk=0;
    call_ground = 0;
    call_floor1 = 0;
    call_floor2 = 0;
    call_floor3 = 0;
    floor_sensor1 = 1;
    floor_sensor2 = 0;
    floor_sensor3 = 0;
    emergency_stop = 0;
  #10  clk=1;
  #10
    clk=0;
    call_ground = 0;
    call_floor1 = 0;
    call_floor2 = 1;
    call_floor3 = 0;
    floor_sensor1 = 0;
    floor_sensor2 = 0;
    floor_sensor3 = 0;
    emergency_stop = 0;
  #10  clk=1;
  #10
    clk=0;
    call_ground = 0;
    call_floor1 = 0;
    call_floor2 = 0;
    call_floor3 = 0;
    floor_sensor1 = 0;
    floor_sensor2 = 1;
    floor_sensor3 = 0;
    emergency_stop = 0;
  #10  clk=1;
  #10
    clk=0;
    call_ground = 0;
    call_floor1 = 0;
    call_floor2 = 0;
    call_floor3 = 1;
    floor_sensor1 = 0;
    floor_sensor2 = 0;
    floor_sensor3 = 0;
    emergency_stop = 0;
  #10  clk=1;
  #10
    clk=0;
    call_ground = 0;
    call_floor1 = 0;
    call_floor2 = 0;
    call_floor3 = 0;
    floor_sensor1 = 0;
    floor_sensor2 = 0;
    floor_sensor3 = 1;
    emergency_stop = 0;
  #10  clk=1;
  #10
    clk=0;
    call_ground = 1;
    call_floor1 = 0;
    call_floor2 = 0;
    call_floor3 = 0;
    floor_sensor1 = 0;
    floor_sensor2 = 0;
    floor_sensor3 = 0;
    emergency_stop = 0;
  #10  clk=1;
  #10
    clk=0;
    call_ground = 0;
    call_floor1 = 0;
    call_floor2 = 0;
    call_floor3 = 0;
    floor_sensor1 = 0;
    floor_sensor2 = 0;
    floor_sensor3 = 1;
    emergency_stop = 0;
  #10  clk=1;
  
  #10 rst=1;
  #10 rst=0;
  #10
    clk=0;
    call_ground = 0;
    call_floor1 = 1;
    call_floor2 = 0;
    call_floor3 = 0;
    floor_sensor1 = 0;
    floor_sensor2 = 0;
    floor_sensor3 = 0;
    emergency_stop = 0;
  #10  clk=1;
  #10
    clk=0;
    call_ground = 0;
    call_floor1 = 0;
    call_floor2 = 0;
    call_floor3 = 0;
    floor_sensor1 = 1;
    floor_sensor2 = 0;
    floor_sensor3 = 0;
    emergency_stop = 0;
  #10  clk=1;
  #10
    clk=0;
    call_ground = 0;
    call_floor1 = 0;
    call_floor2 = 1;
    call_floor3 = 0;
    floor_sensor1 = 0;
    floor_sensor2 = 0;
    floor_sensor3 = 0;
    emergency_stop = 0;
  #10  clk=1;
  #10
    clk=0;
    call_ground = 0;
    call_floor1 = 0;
    call_floor2 = 0;
    call_floor3 = 0;
    floor_sensor1 = 0;
    floor_sensor2 = 1;
    floor_sensor3 = 0;
    emergency_stop = 0;
  #10  clk=1;
  #10
    clk=0;
    call_ground = 0;
    call_floor1 = 0;
    call_floor2 = 0;
    call_floor3 = 1;
    floor_sensor1 = 0;
    floor_sensor2 = 0;
    floor_sensor3 = 0;
    emergency_stop = 0;
  #10  clk=1;
  #10
    clk=0;
    call_ground = 0;
    call_floor1 = 0;
    call_floor2 = 0;
    call_floor3 = 0;
    floor_sensor1 = 0;
    floor_sensor2 = 0;
    floor_sensor3 = 1;
    emergency_stop = 0;
  #10  clk=1;
  #10
    clk=0;
    call_ground = 1;
    call_floor1 = 0;
    call_floor2 = 0;
    call_floor3 = 0;
    floor_sensor1 = 0;
    floor_sensor2 = 0;
    floor_sensor3 = 0;
    emergency_stop = 0;
  #10  clk=1;
  #10
    clk=0;
    call_ground = 0;
    call_floor1 = 0;
    call_floor2 = 0;
    call_floor3 = 0;
    floor_sensor1 = 0;
    floor_sensor2 = 0;
    floor_sensor3 = 0;
    emergency_stop = 1;
  #10  clk=1;
  
  #10 rst=1;
  #10 rst=0;
  #10
    clk=0;
    call_ground = 0;
    call_floor1 = 1;
    call_floor2 = 0;
    call_floor3 = 0;
    floor_sensor1 = 0;
    floor_sensor2 = 0;
    floor_sensor3 = 0;
    emergency_stop = 0;
  #10  clk=1;
  #10
    clk=0;
    call_ground = 0;
    call_floor1 = 0;
    call_floor2 = 0;
    call_floor3 = 0;
    floor_sensor1 = 1;
    floor_sensor2 = 0;
    floor_sensor3 = 0;
    emergency_stop = 0;
  #10  clk=1;
  #10
    clk=0;
    call_ground = 0;
    call_floor1 = 0;
    call_floor2 = 1;
    call_floor3 = 0;
    floor_sensor1 = 0;
    floor_sensor2 = 0;
    floor_sensor3 = 0;
    emergency_stop = 0;
  #10  clk=1;
  #10
    clk=0;
    call_ground = 0;
    call_floor1 = 0;
    call_floor2 = 0;
    call_floor3 = 0;
    floor_sensor1 = 0;
    floor_sensor2 = 1;
    floor_sensor3 = 0;
    emergency_stop = 0;
  #10  clk=1;
  #10
    clk=0;
    call_ground = 0;
    call_floor1 = 0;
    call_floor2 = 0;
    call_floor3 = 1;
    floor_sensor1 = 0;
    floor_sensor2 = 0;
    floor_sensor3 = 0;
    emergency_stop = 0;
  #10  clk=1;
  #10
    clk=0;
    call_ground = 0;
    call_floor1 = 0;
    call_floor2 = 0;
    call_floor3 = 0;
    floor_sensor1 = 0;
    floor_sensor2 = 0;
    floor_sensor3 = 1;
    emergency_stop = 0;
  #10  clk=1;
  #10
    clk=0;
    call_ground = 0;
    call_floor1 = 1;
    call_floor2 = 0;
    call_floor3 = 0;
    floor_sensor1 = 0;
    floor_sensor2 = 0;
    floor_sensor3 = 0;
    emergency_stop = 0;
  #10  clk=1;
  
  #10 rst=1;
  #10 rst=0;
  #10
    clk=0;
    call_ground = 0;
    call_floor1 = 1;
    call_floor2 = 0;
    call_floor3 = 0;
    floor_sensor1 = 0;
    floor_sensor2 = 0;
    floor_sensor3 = 0;
    emergency_stop = 0;
  #10  clk=1;
  #10
    clk=0;
    call_ground = 0;
    call_floor1 = 0;
    call_floor2 = 0;
    call_floor3 = 0;
    floor_sensor1 = 1;
    floor_sensor2 = 0;
    floor_sensor3 = 0;
    emergency_stop = 0;
  #10  clk=1;
  #10
    clk=0;
    call_ground = 0;
    call_floor1 = 0;
    call_floor2 = 1;
    call_floor3 = 0;
    floor_sensor1 = 0;
    floor_sensor2 = 0;
    floor_sensor3 = 0;
    emergency_stop = 0;
  #10  clk=1;
  #10
    clk=0;
    call_ground = 0;
    call_floor1 = 0;
    call_floor2 = 0;
    call_floor3 = 0;
    floor_sensor1 = 0;
    floor_sensor2 = 1;
    floor_sensor3 = 0;
    emergency_stop = 0;
  #10  clk=1;
  #10
    clk=0;
    call_ground = 0;
    call_floor1 = 0;
    call_floor2 = 0;
    call_floor3 = 1;
    floor_sensor1 = 0;
    floor_sensor2 = 0;
    floor_sensor3 = 0;
    emergency_stop = 0;
  #10  clk=1;
  #10
    clk=0;
    call_ground = 0;
    call_floor1 = 0;
    call_floor2 = 0;
    call_floor3 = 0;
    floor_sensor1 = 0;
    floor_sensor2 = 0;
    floor_sensor3 = 1;
    emergency_stop = 0;
  #10  clk=1;
  #10
    clk=0;
    call_ground = 0;
    call_floor1 = 0;
    call_floor2 = 1;
    call_floor3 = 0;
    floor_sensor1 = 0;
    floor_sensor2 = 0;
    floor_sensor3 = 0;
    emergency_stop = 0;
  #10  clk=1;
  
  #10 rst=1;
  #10 rst=0;
  #10
    clk=0;
    call_ground = 0;
    call_floor1 = 1;
    call_floor2 = 0;
    call_floor3 = 0;
    floor_sensor1 = 0;
    floor_sensor2 = 0;
    floor_sensor3 = 0;
    emergency_stop = 0;
  #10  clk=1;
  #10
    clk=0;
    call_ground = 0;
    call_floor1 = 0;
    call_floor2 = 0;
    call_floor3 = 0;
    floor_sensor1 = 1;
    floor_sensor2 = 0;
    floor_sensor3 = 0;
    emergency_stop = 0;
  #10  clk=1;
  #10
    clk=0;
    call_ground = 0;
    call_floor1 = 0;
    call_floor2 = 1;
    call_floor3 = 0;
    floor_sensor1 = 0;
    floor_sensor2 = 0;
    floor_sensor3 = 0;
    emergency_stop = 0;
  #10  clk=1;
  #10
    clk=0;
    call_ground = 0;
    call_floor1 = 0;
    call_floor2 = 0;
    call_floor3 = 0;
    floor_sensor1 = 0;
    floor_sensor2 = 1;
    floor_sensor3 = 0;
    emergency_stop = 0;
  #10  clk=1;
  #10
    clk=0;
    call_ground = 0;
    call_floor1 = 0;
    call_floor2 = 0;
    call_floor3 = 1;
    floor_sensor1 = 0;
    floor_sensor2 = 0;
    floor_sensor3 = 0;
    emergency_stop = 0;
  #10  clk=1;
  #10
    clk=0;
    call_ground = 0;
    call_floor1 = 0;
    call_floor2 = 0;
    call_floor3 = 0;
    floor_sensor1 = 0;
    floor_sensor2 = 0;
    floor_sensor3 = 1;
    emergency_stop = 0;
  #10  clk=1;
  #10
    clk=0;
    call_ground = 0;
    call_floor1 = 0;
    call_floor2 = 0;
    call_floor3 = 0;
    floor_sensor1 = 0;
    floor_sensor2 = 0;
    floor_sensor3 = 0;
    emergency_stop = 1;
  #10  clk=1;
  
  #10 rst=1;
  #10 rst=0;
  #10
    clk=0;
    call_ground = 0;
    call_floor1 = 1;
    call_floor2 = 0;
    call_floor3 = 0;
    floor_sensor1 = 0;
    floor_sensor2 = 0;
    floor_sensor3 = 0;
    emergency_stop = 0;
  #10  clk=1;
  #10
    clk=0;
    call_ground = 0;
    call_floor1 = 0;
    call_floor2 = 0;
    call_floor3 = 0;
    floor_sensor1 = 1;
    floor_sensor2 = 0;
    floor_sensor3 = 0;
    emergency_stop = 0;
  #10  clk=1;
  #10
    clk=0;
    call_ground = 0;
    call_floor1 = 0;
    call_floor2 = 1;
    call_floor3 = 0;
    floor_sensor1 = 0;
    floor_sensor2 = 0;
    floor_sensor3 = 0;
    emergency_stop = 0;
  #10  clk=1;
  #10
    clk=0;
    call_ground = 0;
    call_floor1 = 0;
    call_floor2 = 0;
    call_floor3 = 0;
    floor_sensor1 = 0;
    floor_sensor2 = 1;
    floor_sensor3 = 0;
    emergency_stop = 0;
  #10  clk=1;
  #10
    clk=0;
    call_ground = 0;
    call_floor1 = 0;
    call_floor2 = 0;
    call_floor3 = 1;
    floor_sensor1 = 0;
    floor_sensor2 = 0;
    floor_sensor3 = 0;
    emergency_stop = 0;
  #10  clk=1;
  #10
    clk=0;
    call_ground = 0;
    call_floor1 = 0;
    call_floor2 = 0;
    call_floor3 = 0;
    floor_sensor1 = 0;
    floor_sensor2 = 0;
    floor_sensor3 = 0;
    emergency_stop = 1;
  #10  clk=1;
  
  #10 rst=1;
  #10 rst=0;
  #10
    clk=0;
    call_ground = 0;
    call_floor1 = 1;
    call_floor2 = 0;
    call_floor3 = 0;
    floor_sensor1 = 0;
    floor_sensor2 = 0;
    floor_sensor3 = 0;
    emergency_stop = 0;
  #10  clk=1;
  #10
    clk=0;
    call_ground = 0;
    call_floor1 = 0;
    call_floor2 = 0;
    call_floor3 = 0;
    floor_sensor1 = 1;
    floor_sensor2 = 0;
    floor_sensor3 = 0;
    emergency_stop = 0;
  #10  clk=1;
  #10
    clk=0;
    call_ground = 0;
    call_floor1 = 0;
    call_floor2 = 1;
    call_floor3 = 0;
    floor_sensor1 = 0;
    floor_sensor2 = 0;
    floor_sensor3 = 0;
    emergency_stop = 0;
  #10  clk=1;
  #10
    clk=0;
    call_ground = 0;
    call_floor1 = 0;
    call_floor2 = 0;
    call_floor3 = 0;
    floor_sensor1 = 0;
    floor_sensor2 = 1;
    floor_sensor3 = 0;
    emergency_stop = 0;
  #10  clk=1;
  #10
    clk=0;
    call_ground = 0;
    call_floor1 = 0;
    call_floor2 = 0;
    call_floor3 = 0;
    floor_sensor1 = 0;
    floor_sensor2 = 0;
    floor_sensor3 = 0;
    emergency_stop = 1;
  #10  clk=1;
  
  #10 rst=1;
  #10 rst=0;
  #10
    clk=0;
    call_ground = 0;
    call_floor1 = 1;
    call_floor2 = 0;
    call_floor3 = 0;
    floor_sensor1 = 0;
    floor_sensor2 = 0;
    floor_sensor3 = 0;
    emergency_stop = 0;
  #10  clk=1;
  #10
    clk=0;
    call_ground = 0;
    call_floor1 = 0;
    call_floor2 = 0;
    call_floor3 = 0;
    floor_sensor1 = 1;
    floor_sensor2 = 0;
    floor_sensor3 = 0;
    emergency_stop = 0;
  #10  clk=1;
  #10
    clk=0;
    call_ground = 0;
    call_floor1 = 0;
    call_floor2 = 1;
    call_floor3 = 0;
    floor_sensor1 = 0;
    floor_sensor2 = 0;
    floor_sensor3 = 0;
    emergency_stop = 0;
  #10  clk=1;
  #10
    clk=0;
    call_ground = 0;
    call_floor1 = 0;
    call_floor2 = 0;
    call_floor3 = 0;
    floor_sensor1 = 0;
    floor_sensor2 = 0;
    floor_sensor3 = 0;
    emergency_stop = 1;
  #10  clk=1;
  
  #10 rst=1;
  #10 rst=0;
  #10
    clk=0;
    call_ground = 0;
    call_floor1 = 1;
    call_floor2 = 0;
    call_floor3 = 0;
    floor_sensor1 = 0;
    floor_sensor2 = 0;
    floor_sensor3 = 0;
    emergency_stop = 0;
  #10  clk=1;
  #10
    clk=0;
    call_ground = 0;
    call_floor1 = 0;
    call_floor2 = 0;
    call_floor3 = 0;
    floor_sensor1 = 1;
    floor_sensor2 = 0;
    floor_sensor3 = 0;
    emergency_stop = 0;
  #10  clk=1;
  #10
    clk=0;
    call_ground = 0;
    call_floor1 = 0;
    call_floor2 = 0;
    call_floor3 = 1;
    floor_sensor1 = 0;
    floor_sensor2 = 0;
    floor_sensor3 = 0;
    emergency_stop = 0;
  #10  clk=1;
  
  #10 rst=1;
  #10 rst=0;
  #10
    clk=0;
    call_ground = 0;
    call_floor1 = 1;
    call_floor2 = 0;
    call_floor3 = 0;
    floor_sensor1 = 0;
    floor_sensor2 = 0;
    floor_sensor3 = 0;
    emergency_stop = 0;
  #10  clk=1;
  #10
    clk=0;
    call_ground = 0;
    call_floor1 = 0;
    call_floor2 = 0;
    call_floor3 = 0;
    floor_sensor1 = 1;
    floor_sensor2 = 0;
    floor_sensor3 = 0;
    emergency_stop = 0;
  #10  clk=1;
  #10
    clk=0;
    call_ground = 0;
    call_floor1 = 0;
    call_floor2 = 0;
    call_floor3 = 0;
    floor_sensor1 = 0;
    floor_sensor2 = 0;
    floor_sensor3 = 0;
    emergency_stop = 1;
  #10  clk=1;
  
  #10 rst=1;
  #10 rst=0;
  #10
    clk=0;
    call_ground = 0;
    call_floor1 = 1;
    call_floor2 = 0;
    call_floor3 = 0;
    floor_sensor1 = 0;
    floor_sensor2 = 0;
    floor_sensor3 = 0;
    emergency_stop = 0;
  #10  clk=1;
  #10
    clk=0;
    call_ground = 0;
    call_floor1 = 0;
    call_floor2 = 0;
    call_floor3 = 0;
    floor_sensor1 = 0;
    floor_sensor2 = 0;
    floor_sensor3 = 0;
    emergency_stop = 1;
  #10  clk=1;
  
  #10 rst=1;
  #10 rst=0;
  #10
    clk=0;
    call_ground = 0;
    call_floor1 = 0;
    call_floor2 = 1;
    call_floor3 = 0;
    floor_sensor1 = 0;
    floor_sensor2 = 0;
    floor_sensor3 = 0;
    emergency_stop = 0;
  #10  clk=1;
  
  #10 rst=1;
  #10 rst=0;
  #10
    clk=0;
    call_ground = 0;
    call_floor1 = 0;
    call_floor2 = 0;
    call_floor3 = 1;
    floor_sensor1 = 0;
    floor_sensor2 = 0;
    floor_sensor3 = 0;
    emergency_stop = 0;
  #10  clk=1;
  
  #10 rst=1;
  #10 rst=0;
  #10
    clk=0;
    call_ground = 0;
    call_floor1 = 0;
    call_floor2 = 0;
    call_floor3 = 0;
    floor_sensor1 = 0;
    floor_sensor2 = 0;
    floor_sensor3 = 0;
    emergency_stop = 1;
  #10  clk=1;
  
  
end

endmodule
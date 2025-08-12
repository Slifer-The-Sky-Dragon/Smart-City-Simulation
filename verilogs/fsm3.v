module fsm3(clk, rst, call_ground, call_floor1, call_floor2, call_floor3, floor_sensor1, floor_sensor2, floor_sensor3, emergency_stop, moving, idle, alarm);

input clk, rst, call_ground, call_floor1, call_floor2, call_floor3, floor_sensor1, floor_sensor2, floor_sensor3, emergency_stop;
output moving, idle, alarm;

localparam IdleGround = 4'b0000, IdleFloor1 = 4'b0001, IdleFloor2 = 4'b0010, IdleFloor3 = 4'b0011, MovingUp1 = 4'b0100, MovingUp2 = 4'b0101, MovingUp3 = 4'b0110, MovingDown3 = 4'b0111, MovingDown2 = 4'b1000, MovingDown1 = 4'b1001, Emergency = 4'b1010;

reg [3:0] ns, ps;

always@(ps, call_ground, call_floor1, call_floor2, call_floor3, floor_sensor1, floor_sensor2, floor_sensor3, emergency_stop) begin

  case(ps)
    IdleGround: begin
      if (call_floor1)
        ns <= MovingUp1;
      else if (call_floor2)
        ns <= MovingUp2;
      else if (call_floor3)
        ns <= MovingUp3;
      else if (emergency_stop)
        ns <= Emergency;
      else
        ns <= IdleGround;
    end
    
    IdleFloor1: begin
      if (call_ground)
        ns <= MovingDown1;
      else if (call_floor2)
        ns <= MovingUp2;
      else if (call_floor3)
        ns <= MovingUp3;
      else if (emergency_stop)
        ns <= Emergency;
      else
        ns <= IdleFloor1;
    end
    
    IdleFloor2: begin
      if (call_ground)
        ns <= MovingDown2;
      else if (call_floor1)
        ns <= MovingDown2;
      else if (call_floor3)
        ns <= MovingUp3;
      else if (emergency_stop)
        ns <= Emergency;
      else
        ns <= IdleFloor2;
    end
    
    IdleFloor3: begin
      if (call_ground)
        ns <= MovingDown3;
      else if (call_floor1)
        ns <= MovingDown2;
      else if (call_floor2)
        ns <= MovingDown2;
      else if (emergency_stop)
        ns <= Emergency;
      else
        ns <= IdleFloor3;
    end
    
    MovingUp1: begin
      if (floor_sensor1)
        ns <= IdleFloor1;
      else if (emergency_stop)
        ns <= Emergency;
      else
        ns <= MovingUp1;
    end
    
    MovingUp2: begin
      if (floor_sensor2)
        ns <= IdleFloor2;
      else if (emergency_stop)
        ns <= Emergency;
      else
        ns <= MovingUp2;
    end
    
    MovingUp3: begin
      if (floor_sensor3)
        ns <= IdleFloor3;
      else if (emergency_stop)
        ns <= Emergency;
      else
        ns <= MovingUp3;
    end
    
    MovingDown3: begin
      if (floor_sensor3)
        ns <= IdleFloor3;
      else if (emergency_stop)
        ns <= Emergency;
      else
        ns <= MovingDown3;
    end
    
    MovingDown2: begin
      if (floor_sensor2)
        ns <= IdleFloor2;
      else if (emergency_stop)
        ns <= Emergency;
      else
        ns <= MovingDown2;
    end
    
    MovingDown1: begin
      if (floor_sensor1)
        ns <= IdleGround;
      else if (emergency_stop)
        ns <= Emergency;
      else
        ns <= MovingDown1;
    end
    
    Emergency: begin
      if (call_ground)
        ns <= IdleGround;
      else if (!emergency_stop)
        ns <= Emergency;
      else
        ns <= Emergency;
    end
    
    default: begin
      ns <= IdleGround;
    end
    
  endcase
  
end

assign moving = (ps==MovingUp1)? 1'b1: (ps==MovingUp2)? 1'b1: (ps==MovingUp3)? 1'b1: (ps==MovingDown3)? 1'b1: (ps==MovingDown2)? 1'b1: (ps==MovingDown1)? 1'b1: 1'b0;
assign idle = (ps==IdleGround)? 1'b1: (ps==IdleFloor1)? 1'b1: (ps==IdleFloor2)? 1'b1: (ps==IdleFloor3)? 1'b1: 1'b0;
assign alarm = (ps==Emergency)? 1'b1: 1'b0;

always@(posedge clk, posedge rst) begin

  if (rst) ps <= IdleGround;
  else ps <= ns;
  
end

endmodule

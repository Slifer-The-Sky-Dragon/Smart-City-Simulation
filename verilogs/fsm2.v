module fsm2(clk, rst, pin_correct, door_closed, intruder_detected, lock_state, alarm_state);

input clk, rst, pin_correct, door_closed, intruder_detected;
output lock_state, alarm_state;

localparam Locked = 2'b00, Unlocked = 2'b01, Alarm = 2'b10;

reg [1:0] ns, ps;

always@(ps, pin_correct, door_closed, intruder_detected) begin

  case(ps)
    Locked: begin
      if (pin_correct & door_closed)
        ns <= Unlocked;
      else if (intruder_detected)
        ns <= Alarm;
      else
        ns <= Locked;
    end
    
    Unlocked: begin
      if (!door_closed)
        ns <= Locked;
      else if (intruder_detected)
        ns <= Alarm;
      else
        ns <= Unlocked;
    end
    
    Alarm: begin
      if (pin_correct)
        ns <= Locked;
      else if (!pin_correct)
        ns <= Alarm;
      else
        ns <= Alarm;
    end
    
    default: begin
      ns <= Locked;
    end
    
  endcase
  
end

assign lock_state = (ps==Locked)? 1'b1: 1'b0;
assign alarm_state = (ps==Alarm)? 1'b1: 1'b0;

always@(posedge clk, posedge rst) begin

  if (rst) ps <= Locked;
  else ps <= ns;
  
end

endmodule

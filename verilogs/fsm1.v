module fsm1(clk, rst, timer_done, pedestrian_request, main_green, side_green, warning);

input clk, rst, timer_done, pedestrian_request;
output main_green, side_green, warning;

localparam MainGreen = 3'b000, MainYellow = 3'b001, SideGreen = 3'b010, SideYellow = 3'b011, PedestrianWait = 3'b100;

reg [2:0] ns, ps;

always@(ps, timer_done, pedestrian_request) begin

  case(ps)
    MainGreen: begin
      if (pedestrian_request & timer_done)
        ns <= MainYellow;
      else if (timer_done)
        ns <= MainYellow;
      else if (!timer_done)
        ns <= MainGreen;
      else
        ns <= MainGreen;
    end
    
    MainYellow: begin
      if (timer_done)
        ns <= SideGreen;
      else if (!timer_done)
        ns <= MainYellow;
      else
        ns <= MainYellow;
    end
    
    SideGreen: begin
      if (pedestrian_request & !timer_done)
        ns <= PedestrianWait;
      else if (timer_done)
        ns <= SideYellow;
      else if (!timer_done)
        ns <= SideGreen;
      else
        ns <= SideGreen;
    end
    
    SideYellow: begin
      if (timer_done)
        ns <= MainGreen;
      else if (!timer_done)
        ns <= SideYellow;
      else
        ns <= SideYellow;
    end
    
    PedestrianWait: begin
      if (timer_done)
        ns <= SideYellow;
      else if (!timer_done)
        ns <= PedestrianWait;
      else
        ns <= PedestrianWait;
    end
    
    default: begin
      ns <= MainGreen;
    end
    
  endcase
  
end

assign main_green = (ps==MainGreen)? 1'b1: 1'b0;
assign side_green = (ps==SideGreen)? 1'b1: (ps==PedestrianWait)? 1'b1: 1'b0;
assign warning = (ps==MainYellow)? 1'b1: (ps==SideYellow)? 1'b1: 1'b0;

always@(posedge clk, posedge rst) begin

  if (rst) ps <= MainGreen;
  else ps <= ns;
  
end

endmodule

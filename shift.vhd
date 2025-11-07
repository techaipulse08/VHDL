library IEEE;
use IEEE.STD_LOGIC_1164.ALL;
use IEEE.STD_LOGIC_ARITH.ALL;
use IEEE.STD_LOGIC_UNSIGNED.ALL;

entity shift is
    Port (
        clk : in STD_LOGIC;
        clr : in STD_LOGIC;
        lin : in STD_LOGIC;
        rin : in STD_LOGIC;
        s   : in STD_LOGIC_VECTOR (1 downto 0);
        d   : in STD_LOGIC_VECTOR (3 downto 0);
        q   : inout STD_LOGIC_VECTOR (3 downto 0)
    );
end shift;

architecture Behavioral of shift is
begin
    process(clk, clr, lin, rin, s, d)
    begin
        if (clr = '0') then
            q <= "0000";
        elsif (clk'event and clk = '1') then
            if (s = "00") then
                q <= q;                       -- Hold
            elsif (s = "01") then
                q <= rin & q(3 downto 1);     -- Shift right
            elsif (s = "10") then
                q <= q(2 downto 0) & lin;     -- Shift left
            elsif (s = "11") then
                q <= d;                       -- Load
            end if;
        end if;
    end process;
end Behavioral;


%prompt = "What would you like to do? \n1) Problem 3 Grayscale \n2) Problem 3";

A = imread('Dog.jpg');
imshow(A);
A = double(A);

% Problem 3
B = grayScale(A);
B = uint8(B);
imwrite(B, 'Problem3.jpg');

% Problem 4
C = convertBinary(B, .25*255);
C = uint8(C);
imwrite(C, 'Problem4a.jpg');

C = convertBinary(B, .5*255);
C = uint8(C);
imwrite(C, 'Problem4b.jpg');

C = convertBinary(B, .75*255);
C = uint8(C);
imwrite(C, 'Problem4c.jpg');

% Problem 5
D = Problem5(A, 1, .2);
D = uint8(D);
imwrite(D, 'Problem5a.jpg');

D = Problem5(A, 1, 1);
D = uint8(D);
imwrite(D, 'Problem5b.jpg');

D = Problem5(A, 1, 5);
D = uint8(D);
imwrite(D, 'Problem5c.jpg');


E = Problem6(A);
E = uint8(E);
imwrite(E, 'Problem6.jpg');

problem7(A);

%F = uint8(D);
%imshow(D);

function [imOut] = grayScale(imIn)
    imOut = 0.2989*imIn(:,:,1) + 0.5870*imIn(:,:,1) + 0.1140*imIn(:,:,1);
end

function [imOut] = convertBinary(imIn, thresh)
    imOut = zeros(size(imIn));
    imOut(imIn>thresh)=255;
end

function [imOut] = Problem5(imIn, c, gamma)
    imIn = imIn / 255;
    imOut = c*imIn.^gamma;
    imOut = imOut * 255;
end

function [imOut] = Problem6(imIn)
    floatingImage = imIn / 255;
    
    imOut = zeros(size(imIn));
    
    for r=1:size(floatingImage,1)
        for c=1:size(floatingImage,2)
            
            % Convert RGB to HSV
            
            RedChannel = floatingImage(r,c,1);
            GreenChannel = floatingImage(r,c,2);
            BlueChannel = floatingImage(r,c,3);
            
            Value = max([RedChannel,GreenChannel,BlueChannel]);
    
            delta = max([RedChannel,GreenChannel,BlueChannel]) - min([RedChannel,GreenChannel,BlueChannel]);
            if (delta == 0)
                Hue = 0;
            elseif ( Value == RedChannel)
                Hue = 60 * (GreenChannel - BlueChannel) / delta;
            elseif (Value == GreenChannel)
                Hue = 120 + 60 * (BlueChannel - RedChannel) / delta;
            else 
                Hue = 240 + 60 * (RedChannel - GreenChannel) / delta;
            end
            
            if ( Value == 0 )
                Saturation = 0;
            else
                Saturation = delta/Value;
            end 
            
            % The Part where we add 50 to HUE
            
            Hue = Hue + 50;
            
            if (Hue < 0)
                Hue = Hue + 360;
            end
            
            Hue = mod(Hue,360);
            
            % Now convert HSV back to RGB
            
            delta = Saturation * Value;
            
            if (Hue >= 0 ) && (Hue < 60)
                RedChannel = Value;
                GreenChannel = Hue / 60 * delta + Value - delta;
                BlueChannel = Value - delta;
            elseif (Hue >= 60 ) && (Hue < 120)
                RedChannel = Value - delta - ((Hue-120)*delta / 60);
                GreenChannel = Value;
                BlueChannel = Value - delta;
            elseif (Hue >= 120 ) && (Hue < 180)
                RedChannel = Value - delta;
                GreenChannel = Value;
                BlueChannel = ((Hue-120)*delta / 60) + Value - delta;
            elseif (Hue >= 180 ) && (Hue < 240)
                RedChannel = Value - delta;
                GreenChannel = Value - delta - ((Hue-240)*delta / 60);
                BlueChannel = Value;
            elseif (Hue >= 240 ) && (Hue < 300)
                RedChannel = ((Hue-240)*delta / 60) + Value - delta;
                GreenChannel = Value - delta;
                BlueChannel = Value;
            else
                RedChannel = Value;
                GreenChannel = Value - delta;
                BlueChannel = Value - delta - ((Hue-360)*delta / 60);
            end
            
            imOut(r,c,:) = [RedChannel, GreenChannel, BlueChannel];
            
        end
    end
    
    imOut = imOut * 255;
    
end

function [] = problem7(imIn)
    helpHist(grayScale(imIn));
    helpHist(imIn(:,:,1));
    helpHist(imIn(:,:,2));
    helpHist(imIn(:,:,3));
end

function [] = helpHist(channel)
    bins=zeros(1,256);
    for i=1:size(channel,1)
        for j=1:size(channel,2)
            bins(floor(channel(i,j))+1)=bins(floor(channel(i,j))+1)+1;
        end
    end
    
    bins=bins/sum(bins);
    figure;plot(1:256,bins);
end
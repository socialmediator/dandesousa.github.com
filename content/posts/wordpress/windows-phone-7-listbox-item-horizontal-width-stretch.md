Title: Windows Phone 7: ListBox Item Horizontal Width Stretch
Date: 2010-08-29 17:15
Author: Admin
Category: Programming
Tags: .net, C#, WP7

I have spent most of the day today working on a Windows Phone 7 app I
hope to have ready for launch this fall / winter. I figured that
adoption of the platform and generation of apps is good for all of us as
it generates hype for the platform and facilitates development. So I
will be sharing all the gotcha’s and particularly frustrating
experiences (and there solutions here!).

In WP7, if you try to use a ListBox control, you’ll noticed that child
controls do not completely fill the available space of the control. To
do this you have to override the style of the ListBox’s ItemContainer,
as well as override the template and set the appropriate
HorizontalContentAlignment properties.

First, this is what the problem looks like. In blue we have the entire
ListBox Control, and in white is the space for an individual item.

The Problem
-----------

![problem][]

As you can see, the ListBoxItem is shown in white and only fits the size
of the content. The entire ListBox is shown in red and remains empty. If
you increase the size of the text it will stretch to the width. But if
we wanted to align the button on the right as its own column we want the
text to take up the remaining space and we need the item to fit the
width of the control. Then we’d be able to use a Grid control to set the
proper alignment.

The Solution
------------

We have to override not only the HorizontalContentAlignment Properties
of the ItemContainer but also pass those onto the Template and Container
in the Style. This is very unintuitive as you would expect
HorizontalContentAlignment to just work.

    :::xml
    <phone:PhoneApplicationPage.Resources> <Style
    x:Key="ListBoxItemStyle1" TargetType="ListBoxItem">
    <Setter Property="Background" Value="Transparent"/>
    <Setter Property="BorderThickness" Value="0"/>
    <Setter Property="BorderBrush" Value="Transparent"/>
    <Setter Property="Padding" Value="0"/>
    <Setter Property="HorizontalContentAlignment" Value="Stretch"/>
    <Setter Property="HorizontalAlignment" Value="Stretch" />
    <Setter Property="VerticalContentAlignment" Value="Stretch"/>
    <Setter Property="Template">
    <Setter.Value>
    <ControlTemplate TargetType="ListBoxItem">
    <Border x:Name="LayoutRoot" BorderBrush="{TemplateBinding BorderBrush}"
    BorderThickness="{TemplateBinding BorderThickness}"
    Background="{TemplateBinding Background}"
    HorizontalAlignment="{TemplateBinding HorizontalAlignment}"
    VerticalAlignment="{TemplateBinding VerticalAlignment}">
    <ContentControl x:Name="ContentContainer"
    ContentTemplate="{TemplateBinding ContentTemplate}"
    Content="{TemplateBinding Content}" Foreground="{TemplateBinding
    Foreground}" HorizontalContentAlignment="{TemplateBinding
    HorizontalContentAlignment}" Margin="{TemplateBinding Padding}"
    VerticalContentAlignment="{TemplateBinding VerticalContentAlignment}"/>
    </Border>
    </ControlTemplate>
    </Setter.Value>
    </Setter>
    </Style> </phone:PhoneApplicationPage.Resources> 

Then apply it to the ListBox:

    :::xml
    <ListBox x:Name="SearchResultsListBox"
    Grid.Row="0"
    HorizontalContentAlignment="Stretch"
    ItemContainerStyle="{StaticResource ListBoxItemStyle1}"
    ItemsSource="{Binding ElementName=SearchPageControl,
        Path=QueryHandler.OpenSearchSuggestion.section.items, Mode=OneWay}"\>
        ... 
        

The Result
----------

![solved][]

As you can see the item wrapped in white stretches the entire width of
the ListBox in red.

Conclusions
-----------

Although unintuitive this should get the job done. Hopefully Microsoft
can make some of these details more straightforward before the final
release or in updated versions of .NET.


[problem]: /static/wp-content/uploads/2010/08/problem_thumb.png
"problem"
[solved]: /static/wp-content/uploads/2010/08/solved_thumb.png
"solved"
